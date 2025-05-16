
# 📥 `POST /api/users/register` — Register a New User

Registers a new user in the system by securely storing their encrypted email and hashed password.

---

## 🔐 Security Overview

- **Email is encrypted** using Fernet (AES-based, randomized encryption)
- **Password is hashed** using Bcrypt via `passlib`
- **Uniqueness check** is enforced using a deterministic SHA256 `email_hash` column
- **No sensitive data is stored in plain text** in the database
- Built-in protection against duplicate signups
- Compatible with JWT auth flow

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
5. Prevents duplicate encrypted email using hashed lookup

---

## ✅ Dev Notes

- This endpoint is implemented in `userservice`, under `trust_layer`
- Routes are defined in: `app/users/routes.py`
- Model: `app/models/user.py`
- Schema: `app/schemas/user.py`
- Encryption + hashing logic: `app/utils.py`
- Alembic is used for all DB schema changes

---

# 🔑 `POST /api/users/login` — User Login

Authenticates an existing user and returns a pair of JWT tokens: access + refresh.

---

## 🔐 Security Overview

- Validates credentials against stored encrypted + hashed data
- Issues **access token** (short-lived) and **refresh token** (long-lived)
- JWT tokens signed using secret and algorithm from `.env`

---

## 🧪 Endpoint Details

**URL:** `POST /api/users/login`  
**Auth:** ❌ No auth required  
**Consumes:** `application/x-www-form-urlencoded`  
**Produces:** `application/json`

---

## 📨 Request Body

Use `x-www-form-urlencoded` in Postman or frontend login form:

| Field     | Type   | Required | Notes                           |
|-----------|--------|----------|---------------------------------|
| `username`| string | ✅        | This is the user’s email        |
| `password`| string | ✅        | Must match hashed password in DB|

---

## 📤 Response (200 OK)

```json
{
  "access_token": "<JWT>",
  "refresh_token": "<JWT>",
  "token_type": "bearer"
}
```

---

## 🔁 Error Responses

### 400 Bad Request — Invalid credentials

```json
{
  "detail": "Invalid credentials"
}
```

---

## ⚙️ Internal Behavior

1. Hash lookup via `email_hash = sha256(username.lower().strip())`
2. Password is checked using `verify_password()`
3. If valid:
   - `access_token` = JWT with `exp` in 30 minutes
   - `refresh_token` = JWT with `exp` in 7 days

---

## ✅ Dev Notes

- Route: `@router.post("/login")`
- Uses `OAuth2PasswordRequestForm` to handle `username` + `password`
- JWT creation in `utils.py`: `create_access_token()` and `create_refresh_token()`
- Secret + expiry loaded from `app/config.py` via `.env`

---

## 🛠 Built With

- FastAPI
- SQLAlchemy (async)
- PyJWT
- passlib[bcrypt]
- Docker Compose
