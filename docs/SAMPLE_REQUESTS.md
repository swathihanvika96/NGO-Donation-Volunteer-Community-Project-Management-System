# Sample requests (as shown in Swagger → Try it out)

Log in first (`POST /api/v1/auth/login`), click **Authorize** in Swagger and paste the `access_token`.

Ids (`1`) must refer to records that exist.

## `POST /api/v1/auth/register`
Self-register (volunteer or donor)

```json
{
  "email": "swathi@gmail.com",
  "full_name": "Swathi Hanvika",
  "password": "Passw0rd!",
  "role": "volunteer"
}
```

## `POST /api/v1/auth/login`
Login and receive access + refresh tokens

```json
{
  "email": "swathi@gmail.com",
  "password": "Passw0rd!"
}
```

## `POST /api/v1/auth/refresh`
Exchange a refresh token for a new token pair (rotation)

```json
{
  "refresh_token": "<refresh token from /auth/login>"
}
```

## `POST /api/v1/auth/logout`
Revoke a refresh token

```json
{
  "refresh_token": "<refresh token from /auth/login>"
}
```

## `POST /api/v1/auth/forgot-password`
Start the password reset workflow

```json
{
  "email": "swathi@gmail.com"
}
```

## `POST /api/v1/auth/reset-password`
Complete the password reset with the emailed token

```json
{
  "token": "<reset token>",
  "new_password": "NewPassw0rd!"
}
```

## `POST /api/v1/auth/change-password`
Change own password

```json
{
  "current_password": "Passw0rd!",
  "new_password": "NewPassw0rd!"
}
```

## `POST /api/v1/users`
Create a user with any role

```json
{
  "email": "swathi@gmail.com",
  "full_name": "Swathi Hanvika",
  "password": "Passw0rd!",
  "role": "ngo_manager"
}
```

## `PATCH /api/v1/users/{user_id}`
Update User

```json
{
  "full_name": "Swathi Hanvika",
  "role": "ngo_manager"
}
```

## `POST /api/v1/donors`
Create a donor profile

```json
{
  "name": "Swathi Hanvika",
  "donor_type": "individual",
  "email": "swathi@gmail.com",
  "phone": "+919876543210",
  "address": "12 Lake Road, Hyderabad",
  "city": "Hyderabad",
  "country": "India",
  "tax_id": "ABCDE1234F",
  "contact_person": "Ravi Kumar",
  "notes": "Sample note",
  "status": "active",
  "user_id": 1
}
```

## `PATCH /api/v1/donors/{donor_id}`
Update a donor profile

```json
{
  "name": "Swathi Hanvika",
  "donor_type": "individual",
  "status": "active",
  "email": "swathi@gmail.com",
  "phone": "+919876543210",
  "address": "12 Lake Road, Hyderabad",
  "city": "Hyderabad",
  "country": "India",
  "tax_id": "ABCDE1234F",
  "contact_person": "Ravi Kumar",
  "notes": "Sample note"
}
```

## `POST /api/v1/campaigns`
Create a fundraising campaign (starts as draft)

```json
{
  "title": "Clean Water Drive",
  "description": "Providing clean drinking water to rural villages",
  "category": "education",
  "goal_amount": "100000.00",
  "start_date": "2026-10-28",
  "end_date": "2026-12-27",
  "manager_id": 1
}
```

## `PATCH /api/v1/campaigns/{campaign_id}`
Update Campaign

```json
{
  "title": "Clean Water Drive",
  "description": "Providing clean drinking water to rural villages",
  "category": "education",
  "goal_amount": "100000.00",
  "start_date": "2026-10-28",
  "end_date": "2026-12-27",
  "manager_id": 1
}
```

## `POST /api/v1/donations`
Record a donation

```json
{
  "donor_id": 1,
  "campaign_id": 1,
  "amount": "5000.00",
  "donation_date": "2026-10-27",
  "method": "bank_transfer",
  "reference_number": "TXN-2026-0001",
  "status": "confirmed",
  "notes": "Sample note"
}
```

## `PATCH /api/v1/donations/{donation_id}`
Edit a donation (financial fields only while pending)

```json
{
  "amount": "5000.00",
  "donation_date": "2026-10-27",
  "method": "bank_transfer",
  "notes": "Sample note"
}
```

## `POST /api/v1/donations/{donation_id}/confirm`
Confirm a pending donation (adds it to the campaign total)

```json
{
  "reason": "Distribution for village drive"
}
```

## `POST /api/v1/donations/{donation_id}/cancel`
Cancel a pending donation

```json
{
  "reason": "Distribution for village drive"
}
```

## `POST /api/v1/donations/{donation_id}/reverse`
Reverse a confirmed donation (deducts from campaign total, voids receipt)

```json
{
  "reason": "Distribution for village drive"
}
```

## `POST /api/v1/donations/{donation_id}/refund`
Refund a confirmed donation (deducts from campaign total, voids receipt)

```json
{
  "reason": "Distribution for village drive"
}
```

## `POST /api/v1/receipts`
Generate a receipt for a confirmed donation

```json
{
  "donation_id": 1
}
```

## `POST /api/v1/volunteers`
Register a volunteer (staff)

```json
{
  "full_name": "Swathi Hanvika",
  "email": "swathi@gmail.com",
  "phone": "+919876543210",
  "address": "12 Lake Road, Hyderabad",
  "skills": [
    "teaching",
    "first aid"
  ],
  "experience": "string",
  "availability": "weekends",
  "emergency_contact_name": "string",
  "emergency_contact_phone": "string",
  "emergency_contact_relation": "string",
  "user_id": 1
}
```

## `POST /api/v1/volunteers/me`
Create my own volunteer profile

```json
{
  "full_name": "Swathi Hanvika",
  "email": "swathi@gmail.com",
  "phone": "+919876543210",
  "address": "12 Lake Road, Hyderabad",
  "skills": [
    "teaching",
    "first aid"
  ],
  "experience": "string",
  "availability": "weekends",
  "emergency_contact_name": "string",
  "emergency_contact_phone": "string",
  "emergency_contact_relation": "string",
  "user_id": 1
}
```

## `PATCH /api/v1/volunteers/{volunteer_id}`
Update a volunteer (own profile or staff)

```json
{
  "full_name": "Swathi Hanvika",
  "phone": "+919876543210",
  "address": "12 Lake Road, Hyderabad",
  "skills": [
    "teaching",
    "first aid"
  ],
  "experience": "string",
  "availability": "weekends",
  "status": "active",
  "emergency_contact_name": "string",
  "emergency_contact_phone": "string",
  "emergency_contact_relation": "string"
}
```

## `POST /api/v1/assignments`
Assign a volunteer to a project (rejects overlapping assignments)

```json
{
  "volunteer_id": 1,
  "project_id": 1,
  "responsibility": "Site helper",
  "start_date": "2026-10-28",
  "end_date": "2026-12-27"
}
```

## `PATCH /api/v1/assignments/{assignment_id}`
Update Assignment

```json
{
  "responsibility": "Site helper",
  "start_date": "2026-10-28",
  "end_date": "2026-12-27"
}
```

## `POST /api/v1/assignments/{assignment_id}/status`
Activate, complete or cancel an assignment

```json
{
  "status": "assigned"
}
```

## `POST /api/v1/attendance`
Record attendance and hours for an assignment day

```json
{
  "assignment_id": 1,
  "attendance_date": "2026-10-28",
  "status": "present",
  "hours": "6.5",
  "notes": "Sample note"
}
```

## `PATCH /api/v1/attendance/{attendance_id}`
Correct an attendance record

```json
{
  "status": "present",
  "hours": "6.5",
  "notes": "Sample note"
}
```

## `POST /api/v1/projects`
Create a community project (starts in planning)

```json
{
  "name": "Village Well Construction",
  "description": "Providing clean drinking water to rural villages",
  "objectives": "Provide safe drinking water to 500 families",
  "location": "Hyderabad",
  "start_date": "2026-10-28",
  "end_date": "2026-12-27",
  "budget": "60000.00",
  "manager_id": 1,
  "campaign_id": 1
}
```

## `PATCH /api/v1/projects/{project_id}`
Update Project

```json
{
  "name": "Village Well Construction",
  "description": "Providing clean drinking water to rural villages",
  "objectives": "Provide safe drinking water to 500 families",
  "location": "Hyderabad",
  "start_date": "2026-10-28",
  "end_date": "2026-12-27",
  "budget": "60000.00",
  "manager_id": 1,
  "campaign_id": 1
}
```

## `POST /api/v1/projects/{project_id}/status`
Change status (activation requires approval)

```json
{
  "status": "planning"
}
```

## `POST /api/v1/projects/{project_id}/submit`
Submit a project for approval

```json
{
  "comments": "Looks good"
}
```

## `POST /api/v1/projects/{project_id}/approve`
Approve a submitted project

```json
{
  "comments": "Looks good"
}
```

## `POST /api/v1/projects/{project_id}/reject`
Reject a submitted project (comment required)

```json
{
  "comments": "Looks good"
}
```

## `POST /api/v1/milestones`
Create Milestone

```json
{
  "project_id": 1,
  "title": "Site survey",
  "description": "Providing clean drinking water to rural villages",
  "due_date": "2026-11-27"
}
```

## `PATCH /api/v1/milestones/{milestone_id}`
Update Milestone

```json
{
  "title": "Site survey",
  "description": "Providing clean drinking water to rural villages",
  "due_date": "2026-11-27",
  "status": "pending"
}
```

## `POST /api/v1/tasks`
Create and assign a task

```json
{
  "milestone_id": 1,
  "title": "Survey the site",
  "description": "Providing clean drinking water to rural villages",
  "assignee_id": 1,
  "priority": "low",
  "deadline": "2026-11-11"
}
```

## `PATCH /api/v1/tasks/{task_id}`
Update task status / progress (assignees may update their own)

```json
{
  "title": "Survey the site",
  "description": "Providing clean drinking water to rural villages",
  "assignee_id": 1,
  "priority": "low",
  "deadline": "2026-11-11",
  "status": "todo",
  "progress": 50
}
```

## `POST /api/v1/expenses`
Submit a project expense

```json
{
  "project_id": 1,
  "category": "materials",
  "amount": "5000.00",
  "expense_date": "2026-10-27",
  "description": "Cement and bricks",
  "receipt_reference": "BILL-1001",
  "attachment_url": "https://files.example.org/receipt.pdf"
}
```

## `PATCH /api/v1/expenses/{expense_id}`
Edit a not-yet-reviewed expense

```json
{
  "category": "materials",
  "amount": "5000.00",
  "expense_date": "2026-10-27",
  "description": "Cement and bricks",
  "receipt_reference": "BILL-1001",
  "attachment_url": "https://files.example.org/receipt.pdf"
}
```

## `POST /api/v1/expenses/{expense_id}/approve`
Approve an expense (finance only, budget-checked)

```json
{
  "comment": "Verified against receipt",
  "override_budget": false
}
```

## `POST /api/v1/expenses/{expense_id}/reject`
Reject an expense (comment required)

```json
{
  "comment": "Verified against receipt"
}
```

## `PUT /api/v1/budgets`
Define (or replace) a campaign or project budget

```json
{
  "scope": "campaign",
  "campaign_id": 1,
  "project_id": 1,
  "amount": "5000.00",
  "notes": "Sample note"
}
```

## `POST /api/v1/resources`
Register a resource (optional opening stock)

```json
{
  "name": "Rice Bags",
  "category": "food_package",
  "description": "Providing clean drinking water to rural villages",
  "unit": "kit",
  "initial_quantity": 100,
  "low_stock_threshold": 10
}
```

## `PATCH /api/v1/resources/{resource_id}`
Update Resource

```json
{
  "name": "Rice Bags",
  "category": "food_package",
  "description": "Providing clean drinking water to rural villages",
  "unit": "kit",
  "low_stock_threshold": 10
}
```

## `POST /api/v1/resources/{resource_id}/stock-in`
Stock In

```json
{
  "quantity": 10,
  "reason": "Distribution for village drive",
  "reference": "string"
}
```

## `POST /api/v1/resources/{resource_id}/stock-out`
Stock out (never below zero)

```json
{
  "quantity": 10,
  "reason": "Distribution for village drive",
  "reference": "string"
}
```

## `POST /api/v1/resource-allocations`
Allocate stock to a project

```json
{
  "resource_id": 1,
  "project_id": 1,
  "quantity": 10,
  "notes": "Sample note"
}
```

## `POST /api/v1/beneficiaries`
Register a beneficiary

```json
{
  "full_name": "Lakshmi Devi",
  "category": "woman",
  "age": 34,
  "gender": "female",
  "phone": "+919876543210",
  "address": "12 Lake Road, Hyderabad",
  "national_id": "XXXX-1234",
  "notes": "Sample note",
  "project_ids": [
    1
  ]
}
```

## `PATCH /api/v1/beneficiaries/{beneficiary_id}`
Update Beneficiary

```json
{
  "full_name": "Lakshmi Devi",
  "category": "woman",
  "age": 34,
  "gender": "female",
  "phone": "+919876543210",
  "address": "12 Lake Road, Hyderabad",
  "national_id": "XXXX-1234",
  "notes": "Sample note"
}
```

## `POST /api/v1/assistance`
Record assistance given to a beneficiary

```json
{
  "beneficiary_id": 1,
  "project_id": 1,
  "resource_id": 1,
  "assistance_type": "food",
  "quantity": 10,
  "distribution_date": "2026-10-28",
  "description": "Monthly ration kit"
}
```

## `POST /api/v1/impact/updates`
Submit a project impact update

```json
{
  "project_id": 1,
  "beneficiaries_served": 40,
  "volunteer_hours": "12.50",
  "resources_distributed": 30,
  "funds_utilized": "900.00",
  "milestones_achieved": 2,
  "notes": "Sample note"
}
```
