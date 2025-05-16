
# 🧾 User Authentication API — Pokémon TCG Market PH

This document covers all endpoints under `/api/users/` for user registration, login, token handling, and identity lookup.

---

## 📥 `POST /api/users/register` — Register a New User

Registers a new user in the system by securely storing their encrypted email and hashed password.

### 🔐 Security

- Email is encrypted using Fernet
- Password is hashed using Bcrypt
- Duplicate emails prevented using SHA256 `email_hash`

### 🧪 Details

- **Method:** `POST`
- **Auth:** ❌ Public
- **Content-Type:** `application/json`

### 📤 Request

```json
{
  "email": "misty@ceruleangym.ph",
  "password": "ToGePiPower2025"
}
```

### ✅ Success Response (201)

```json
{
  "id": 1,
  "email": "misty@ceruleangym.ph",
  "created_at": "2025-05-16T10:55:00.123Z"
}
```

---

## 🔑 `POST /api/users/login` — Authenticate and Get JWTs

Logs in a user and returns both an access token and a refresh token.

### 🧪 Details

- **Method:** `POST`
- **Auth:** ❌ Public
- **Content-Type:** `application/x-www-form-urlencoded`

### 📤 Request

| Key       | Value                      |
|-----------|----------------------------|
| username  | misty@ceruleangym.ph       |
| password  | ToGePiPower2025            |

### ✅ Success Response (200)

```json
{
  "access_token": "<JWT>",
  "refresh_token": "<JWT>",
  "token_type": "bearer"
}
```

---

## 🔁 `POST /api/users/refresh` — Get New Access Token

Uses a refresh token to issue a new short-lived access token.

### 🧪 Details

- **Method:** `POST`
- **Auth:** ✅ Requires valid `refresh-token` header

### 📤 Headers

```
refresh-token: <your-refresh-token>
```

### ✅ Success Response (200)

```json
{
  "access_token": "<new-access-token>",
  "token_type": "bearer"
}
```

---

## 👤 `GET /api/users/me` — Get Current User

Returns info about the currently authenticated user.

### 🧪 Details

- **Method:** `GET`
- **Auth:** ✅ Requires valid `Authorization` header with bearer token

### 📤 Headers

```
Authorization: Bearer <access-token>
```

### ✅ Success Response (200)

```json
{
  "email": "misty@ceruleangym.ph"
}
```

---

## 🛠 Built With

- FastAPI
- SQLAlchemy (async)
- passlib[bcrypt]
- PyJWT
- Alembic
- Docker Compose
