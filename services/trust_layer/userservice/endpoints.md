
# 📥 `POST /api/users/register` — Register a New User

Registers a new user in the system by securely storing their encrypted email and hashed password.

---

## 🔐 Security Overview

- **Email is encrypted** using Fernet (AES-based, randomized encryption)
- **Password is hashed** using Bcrypt via `passlib`
- **Uniqueness check** is enforced using a deterministic SHA256 `email_hash` column
- **No sensitive data is stored in plain text** in the database

---

## 🧪 Endpoint Details

**URL:** `POST /api/users/register`  
**Auth:** ❌ No auth required  
**Consumes:** `application/json`  
**Produces:** `application/json`

---

## 📨 Request Body

```json
{
  "email": "misty@ceruleangym.ph",
  "password": "ToGePiPower2025"
}
```

### Fields:

| Field     | Type   | Required | Notes                         |
|-----------|--------|----------|-------------------------------|
| `email`   | string | ✅        | Must be a valid email address |
| `password`| string | ✅        | Min 8 characters              |

---

## 📤 Response (201 Created)

```json
{
  "id": 1,
  "email": "misty@ceruleangym.ph",
  "created_at": "2025-05-16T10:55:00.123Z"
}
```

---

## 🔁 Error Responses

### 400 Bad Request — Duplicate email

```json
{
  "detail": "Email already registered"
}
```

### 422 Unprocessable Entity — Invalid input

```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

---

## ⚙️ Internal Behavior

1. `email_hash = sha256(email.lower().strip())` is stored for uniqueness lookup
2. `encrypted_email = Fernet.encrypt(email)` is stored in `_email`
3. `password = hash_password(password)` is stored using Bcrypt
4. DB commit and refresh returns newly created user

---

## ✅ Dev Notes

- This endpoint is implemented in `userservice`, under `trust_layer`
- Routes are defined in: `app/users/routes.py`
- Model: `app/models/user.py`
- Schema: `app/schemas/user.py`
- Encryption logic: `app/utils.py`

---

## 🛠 Built With

- FastAPI
- SQLAlchemy (async)
- Alembic (for migrations)
- PostgreSQL
- Docker Compose
