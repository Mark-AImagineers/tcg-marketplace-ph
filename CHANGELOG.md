# 📓 Changelog

This changelog tracks the progress of Pokémon TCG Market PH — built in public, one commit at a time.

---


## [0.1.2] - 2025-05-16

### ✨ Added
- `/login` endpoint implemented using `OAuth2PasswordRequestForm`
- Issued JWT access and refresh tokens via `create_access_token()` and `create_refresh_token()`
- `/refresh` endpoint added to issue new access tokens using valid refresh tokens
- `/me` endpoint added to return authenticated user using `get_current_user()` dependency
- Included token decoding logic with `decode_token()` for access/refresh flows

### 🛠 Changed
- Updated `utils.py` with all JWT helpers: token creation, decoding, hashing
- Centralized JWT config via `.env` for both token durations and secrets
- Cleaned up Postman testing flow for all auth endpoints

### 📄 Docs
- Created markdown documentation for `/register`, `/login`, `/refresh`, `/me` under `/api/users`
- Updated beginner-friendly Alembic migration guide

---
## [0.1.1] - 2025-05-16

### ✨ Added
- Implemented `/register` endpoint with full encryption and validation
- Email field is encrypted using Fernet; password is securely hashed via Bcrypt
- Added `email_hash` using SHA256 to enable deterministic, secure uniqueness checking
- Introduced Alembic for schema migrations; created initial migration for `users` table
- Updated `.env` and Docker Compose to support environment-based configuration
- Dockerized the `userservice` under `trust_layer` with hot-reload support via volume mount
- Built real PostgreSQL integration with local persistence using Docker volumes

### 🛠 Changed
- Refactored `utils.py` to include: `encrypt_data()`, `decrypt_data()`, `hash_email()`
- Created helper for loading `metadata.json` safely with error validation
- `User` model now uses encrypted `_email` column with smart setter/getter and `email_hash` lookup field
- Updated Pydantic models to use `from_attributes` (Pydantic v2) for response serialization

### 🐞 Fixed
- Resolved Fernet encryption issue with non-deterministic email deduplication
- Fixed import and Docker COPY path issues preventing FastAPI app from starting inside container
- Corrected Alembic async integration using native `AsyncEngine` from app context

---
## [0.1.0] - 2025-05-15

### ✨ Added
- Initial folder structure created for modular monorepo setup
- Added `services/` directory with subfolders
- Added top-level scaffolds
- Started writing `README.md` and `CONTRIBUTING.md`

---
> This is a living file — every phase, decision, and update gets logged here as we build forward.
