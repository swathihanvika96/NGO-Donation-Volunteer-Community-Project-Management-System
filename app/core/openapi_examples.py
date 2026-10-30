"""Fill Swagger "Example Value" panels with realistic sample data (Swathi, swathi@gmail.com, ...).

Examples are added to the generated OpenAPI document only; validation and runtime behaviour are untouched.
"""
from datetime import date, timedelta

_T = date.today()
_D = lambda n: (_T + timedelta(days=n)).isoformat()  # noqa: E731

BY_NAME: dict = {
    "email": "swathi@gmail.com", "username": "swathi", "full_name": "Swathi Hanvika", "name": "Swathi Hanvika",
    "password": "Passw0rd!", "new_password": "NewPassw0rd!", "current_password": "Passw0rd!",
    "phone": "+919876543210", "address": "12 Lake Road, Hyderabad", "city": "Hyderabad", "location": "Hyderabad",
    "organization": "Hope Foundation", "national_id": "XXXX-1234", "gender": "female", "age": 34,
    "title": "Clean Water Drive", "description": "Providing clean drinking water to rural villages",
    "goal_amount": "100000.00", "amount": "5000.00", "budget": "60000.00", "raised_amount": "25000.00",
    "reference_number": "TXN-2026-0001", "receipt_reference": "BILL-1001", "comment": "Verified against receipt",
    "comments": "Looks good", "notes": "Sample note", "reason": "Distribution for village drive",
    "start_date": _D(0), "end_date": _D(60), "due_date": _D(30), "deadline": _D(14), "donation_date": _D(-1),
    "expense_date": _D(-1), "distribution_date": _D(0), "attendance_date": _D(0),
    "skills": ["teaching", "first aid"], "responsibility": "Site helper", "hours": "6.5",
    "quantity": 10, "initial_quantity": 100, "low_stock_threshold": 10, "unit": "kit",
    "progress": 50, "refresh_token": "<refresh token from /auth/login>", "token": "<reset token>",
    "attachment_url": "https://files.example.org/receipt.pdf", "beneficiaries_served": 40, "volunteer_hours": "12.50",
    "resources_distributed": 30, "funds_utilized": "900.00", "milestones_achieved": 2, "assistance_type": "food",
}
OVERRIDES: dict = {  # (schema-name prefix, field) -> example
    ("User", "role"): "ngo_manager", ("Register", "role"): "volunteer",
    ("Project", "name"): "Village Well Construction", ("Resource", "name"): "Rice Bags",
    ("Milestone", "title"): "Site survey", ("Task", "title"): "Survey the site", ("Campaign", "title"): "Clean Water Drive",
    ("Donor", "tax_id"): "ABCDE1234F", ("Donor", "country"): "India", ("Donor", "contact_person"): "Ravi Kumar",
    ("Project", "objectives"): "Provide safe drinking water to 500 families", ("Volunteer", "availability"): "weekends",
    ("Expense", "category"): "materials", ("Expense", "description"): "Cement and bricks",
    ("Donation", "method"): "bank_transfer", ("Donation", "status"): "confirmed", ("Beneficiary", "category"): "woman",
    ("Beneficiary", "full_name"): "Lakshmi Devi", ("Assistance", "description"): "Monthly ration kit",
}


def _example(name: str, prop: dict):
    if name in BY_NAME:
        return BY_NAME[name]
    if name.endswith("_id") or name == "id":
        return 1
    if name.endswith("_ids"):
        return [1]
    if name.endswith("_at"):
        return "2026-10-28T09:30:00"
    if "enum" in prop:
        return prop["enum"][0]
    t = prop.get("type")
    if t == "string":
        return {"date": _D(0), "date-time": "2026-10-28T09:30:00", "email": "swathi@gmail.com"}.get(prop.get("format"), "string")
    if t == "integer":
        return prop.get("minimum", 0) if prop.get("minimum", 0) > 0 else 1
    if t == "number":
        return 1.0
    if t == "boolean":
        return False
    return None


def add_examples(spec: dict) -> dict:
    schemas = spec.get("components", {}).get("schemas", {})
    for sname, schema in schemas.items():
        for name, prop in (schema.get("properties") or {}).items():
            if "example" in prop or "examples" in prop:
                continue
            for (prefix, field), val in OVERRIDES.items():
                if field == name and sname.startswith(prefix):
                    prop["example"] = val
                    break
            if "example" in prop:
                continue
            target = prop
            if "anyOf" in prop:  # Optional[...] fields: look at the first non-null branch
                branch = next((b for b in prop["anyOf"] if b.get("type") != "null"), {})
                target = {**branch, **{k: v for k, v in prop.items() if k != "anyOf"}}
            if "$ref" in target:
                enum_ref = schemas.get(target["$ref"].split("/")[-1], {})
                if enum_ref.get("enum"):
                    prop["example"] = enum_ref["enum"][0] if name not in BY_NAME else BY_NAME[name]
                continue
            if target.get("type") == "array" and name in BY_NAME:
                prop["example"] = BY_NAME[name]
                continue
            ex = _example(name, target)
            if ex is not None:
                prop["example"] = ex
    return spec
