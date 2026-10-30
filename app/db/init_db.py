"""Database bootstrap helpers (dev convenience; production uses Alembic migrations)."""
import logging

from sqlalchemy import create_engine, select, text
from sqlalchemy.engine import make_url
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import hash_password
from app.db.base import Base
from app.db.session import engine
from app.models.user import User
from app.utils.enums import Role

logger = logging.getLogger(__name__)


def _create_database_if_missing() -> None:
    """Development convenience: create the MySQL/PostgreSQL database itself when it does not exist yet."""
    url = make_url(settings.DATABASE_URL)
    if url.get_backend_name() == "sqlite" or not url.database:
        return
    try:
        with engine.connect():
            return
    except OperationalError:
        if settings.is_production:
            raise
    name = url.database
    if not name.replace("_", "").isalnum():
        raise RuntimeError(f"Refusing to auto-create database with unsafe name {name!r}")
    admin_url = url.set(database="postgres" if url.get_backend_name() == "postgresql" else None)
    admin = create_engine(admin_url, isolation_level="AUTOCOMMIT")
    with admin.connect() as conn:
        if url.get_backend_name() == "postgresql":
            conn.execute(text(f'CREATE DATABASE "{name}"'))
        else:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"))
    admin.dispose()
    logger.info("Created database %s", name)


def create_tables() -> None:
    import app.models  # noqa: F401  (register all models)

    _create_database_if_missing()
    Base.metadata.create_all(bind=engine)


def ensure_super_admin(db: Session, email: str | None = None, password: str | None = None, name: str | None = None) -> User:
    email = (email or settings.SUPER_ADMIN_EMAIL).lower()
    user = db.scalar(select(User).where(User.email == email))
    if user:
        return user
    user = User(
        email=email,
        full_name=name or settings.SUPER_ADMIN_NAME,
        hashed_password=hash_password(password or settings.SUPER_ADMIN_PASSWORD),
        role=Role.SUPER_ADMIN,
        is_active=True,
    )
    db.add(user)
    db.commit()
    logger.info("Created super admin %s", email)
    return user
