# Pokémon TCG Market PH

**Catalogue, Trade, and Sell Pokémon cards with fellow Pinoys — fast, easy, and built with trust in mind.**
> Built in public. Made by a Filipino collector, for Filipino collectors.

## 📖 Intro & Vision

**Pokémon TCG Market PH** is an open-source platform for Filipino collectors, players, and sellers to easily catalogue, trade, and sell their Pokémon cards.

This started as a personal project — I wanted a tool where I could scan my physical cards, track my collection, and eventually trade or sell them with others in the PH community. What started as a simple idea grew into a full ecosystem: from webcam-based cataloguing, to a trusted marketplace, to future price tracking and collection value monitoring.

The goal is to make card collecting in the Philippines:
- 🧠 Smarter (with data and automation)
- 🔄 Easier (with tools to manage and trade)
- 🤝 Safer (with trust features for local deals)

I'm building this **in public** — with real commits, real transparency, and a strong desire to turn this into something useful for the community. Right now, it’s free and a work-in-progress. Eventually, this could evolve into a paid tool for power users, but the core mission stays the same: **empower the local Pokémon TCG scene**.

## 🧩 Core Features (Updated as of 15.05.2025)

### ✅ Working
- Local dev setup with Docker (FastAPI + PostgreSQL)
- Base structure for user auth and catalogue CRUD
- Initial README and public roadmap

### 🛠️ In Progress
- Card catalogue engine with OCR-ready pipeline
- Webcam scan preview (React frontend)
- Manual catalogue fallback
- Initial marketplace listing schema

### 🧠 Planned
- Real-time OCR auto-cataloguing (premium feature)
- Price crawling from external marketplaces (TCGPlayer, eBay, etc.)
- Pricing insights and collection valuation
- Marketplace messaging + negotiation tools
- Trust system (escrow deposits, verified sellers)
- Contributor-friendly issue labeling and documentation

### Optional Features and Ideas
- Deck Builder
- Deck Build Sell/Trade
- Support for Local TCG shops (setup online shop profiles)
- AI trading chatbot
- AI pokemon guru chatbot

## 🏗️ Development Phases

I'm building this project layer by layer — not feature-hopping, just stacking foundations properly so it actually works. This section shows how it's planned and what’s coming next.

💡 Got ideas or feedback?
This project is being built in public — if you have suggestions, feature ideas, or just want to jam, feel free to open an issue or reach out. Contributions, comments, and crazy ideas are all welcome!
---

## 🔹 Phase 0 – Local Dev Foundation: API, Auth, and DB

**Goal:** Establish a clean, modular local development environment — with FastAPI as the core service, PostgreSQL as the database, and working user authentication (JWT-based). This phase sets the groundwork for building real features. Everything in this phase is about setting rails: once these are in place, the rest of the platform (card catalogue, OCR, listings) can be built modularly, securely, and with confidence in our architecture.

### ✅ Infrastructure & Environment
- ✔️ GitHub repo with initial README and public roadmap
- ✔️ `docker-compose.yml` in `/infra/` to manage local dev containers
- ✔️ `.env.dev` config for environment variables (excluded from Git)
- ✔️ Base PostgreSQL service (local volume + container)

### 🧱 API Bootstrapping (FastAPI)
- ✔️ Project structure scaffolded under `services/api/app/`
- ✔️ Application factory pattern and module layout
- ✔️ Connection to PostgreSQL via async SQLAlchemy (or preferred ORM)
- ✔️ Alembic for migrations

### 🔐 User Authentication
- ✔️ `/register` endpoint (new user signup)
- [ ] JWT-based auth system (access + refresh token support)
- [ ] `/login` endpoint (token generation)
- [ ] Password hashing and validation
- [ ] Reusable `User` model and DB schema

### 🧪 Testing & Validation
- [ ] Basic unit tests for auth flow (register/login)
- [ ] Error handling and input validation (via Pydantic)
- [ ] Local interactive docs via Swagger/OpenAPI (`/docs`)

---

### 🔹 Phase 1 – Catalogue MVP

**Goal:** Manually track your physical cards via API

- [ ] `GET /cards` — show card list
- [ ] `POST /my-catalogue/` — add a card
- [ ] `GET /my-catalogue/` — see your collection
- [ ] `PATCH /my-catalogue/<id>` — edit card
- [ ] `DELETE /my-catalogue/<id>` — remove card

---

### 🔹 Phase 2 – Webcam OCR (Free Tier)

**Goal:** Scan cards using webcam with a scan button

- [ ] React webcam preview + "Scan" button
- [ ] Send snapshot to backend
- [ ] OCR to extract name/number
- [ ] Match with closest card in DB
- [ ] Auto-add to collection

---

### 🔹 Phase 3 – Marketplace Layer

**Goal:** Trade and sell cards from your collection

- [ ] Mark cards as "for sale"
- [ ] Add pricing to listed cards
- [ ] Public marketplace page
- [ ] Buyer profile view
- [ ] Initial messaging system

---

### 🔹 Phase 4 – Trust & Verification

**Goal:** Protect users from scams and build trust

- [ ] Identity or contact verification
- [ ] Deposit/paywall for escrow participation
- [ ] Held funds system (simple ledger)
- [ ] Dispute flow

---

### 🔹 Phase 5 – OCR+ (Premium Tier)

**Goal:** Full real-time OCR scanning (no button)

- [ ] Real-time webcam stream
- [ ] Smart frame detection
- [ ] Auto-capture and auto-match
- [ ] Direct add to collection

---

### 🔹 Phase 6 – Price Engine

**Goal:** Price insights, alerts, and flip tracking

- [ ] Crawl TCGPlayer, eBay, etc.
- [ ] Store price history
- [ ] Show card price graph
- [ ] Alert on spikes or drops
- [ ] Track full portfolio value

---

### 🔹 Phase 7 – UI Polish & Public Beta

- [ ] Responsive React UI
- [ ] Mobile support
- [ ] Theming (dark mode)
- [ ] Public beta access
- [ ] Feedback and iteration loop


📓 **Changelog**

Want to see how the project is progressing day by day?

Check out the full build log in [`CHANGELOG.md`](./CHANGELOG.md) — I’m documenting every key commit, update, and decision there as part of building in public.

## 🧰 Tech Stack

This is the current and planned stack powering the project: (May still change in the future)

| Layer         | Tech                     | Notes                                      |
|---------------|--------------------------|--------------------------------------------|
| Backend API   | FastAPI                  | Main service, containerized via Docker     |
| Frontend      | React                    | For webcam UI and marketplace interface    |
| Database      | PostgreSQL               | Main data store (users, cards, listings)   |
| OCR Engine    | Tesseract + OpenCV       | For card scanning (later: ML models)       |
| Dev Tools     | Docker + Docker Compose  | Containerized local dev setup              |
| Auth          | JWT                      | Token-based user authentication            |
| Testing       | Pytest                   | For backend tests                          |
| Deployment    | TBD (Fly.io / Railway)   | Will decide after MVP                      |

🧑‍💻 **About the Build**

This project is maintained by a solo dev — primarily a Python backend developer, but capable of shipping fullstack. Most of the early focus will be on building solid backend systems and OCR tools before polishing the frontend.


## 🚀 Getting Started

To run the project locally:

### 1. Clone the repo

```bash
git clone https://github.com/your-username/pokemon-tcg-market-ph.git
cd pokemon-tcg-market-ph
```

### 2. Create a `.env` file

You'll need to define some environment variables. Example:

```ini
DATABASE_URL=postgresql://postgres:password@db:5432/tcg
SECRET_KEY=super-secret-key
```

> This will improve and expand as the project grows (e.g. OCR configs, token settings, etc.)

### 3. Run with Docker Compose

```bash
docker-compose up --build
```

### 4. Access the API Docs

Once it’s running, visit:

```
http://localhost:8000/docs
```

## 🤝 Contributing

Contributions are super welcome — this project is being built in public, and I’d love help from fellow devs, designers, or collectors who want to make something cool for the PH Pokémon TCG scene.

### Ways You Can Help

- 🐍 Backend help (FastAPI, database models, auth)
- 📸 OCR / image recognition tuning
- ⚛️ Frontend React components
- 🧪 Testing / CI improvements
- 🕷 Web crawling for market prices
- 💡 Feature ideas, bug reports, or feedback

### How to Contribute

1. ⭐ Star the repo to support the project!
2. 🐛 Check open [Issues](../../issues) or create one
3. 🍴 Fork the repo, create a branch, and open a PR
4. 📢 Share with friends or local groups

> If you're new to contributing, feel free to open a “draft” PR or issue — I’ll help guide you through it!

A `CONTRIBUTING.md` file with coding standards and PR tips will be added soon.

## 🌱 Community

This is a build-in-public project — you can follow progress, give feedback, or just lurk:

- 📓 See progress in [`CHANGELOG.md`](./CHANGELOG.md)
- 🐣 Say hi on Discord: `chizz902#9538`
- 💬 Reddit thread coming soon under [`u/chiz902`](https://www.reddit.com/user/chiz902/)
- 💌 Email: `hello@aimagineers.io`

## 📄 License

This project is open source under the **MIT License** — feel free to fork, use, remix, or build on top of it.

If you end up using this in your own work (or business), I’d love to hear about it!

---

### 🛠 From the same folks who build real impact

I run a studio called [AImagineers](check us out https://aimagineers.io) — where we build AI-powered systems, custom tools, and long-term tech for people solving real problems.
While this project started as a hobby, it’ll be powered by the same principles we use in our studio work: build slow, build right, security, and build things that matter.
