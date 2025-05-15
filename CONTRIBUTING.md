# 🤝 Contributing to Pokémon TCG Market PH

Hey there! 👋

First off — thank you for checking out this project. Whether you're here to report a bug, suggest a feature, write code, or just lurk around, you're more than welcome.

**Pokémon TCG Market PH** is a personal passion project being built in public, with a focus on helping Filipino collectors and players easily catalogue, trade, and sell cards. I’m a solo developer (for now), so I truly appreciate every bit of help.

> Honestly speaking, I’m not a smart person — just someone who’s passionate about building and learning from smarter people. I ask a lot of questions, and I want to keep learning as I go.

If you have feedback, suggestions, or even criticism — I’m open to it. This isn’t a perfect system — it’s an evolving one. So if you're here to improve things, you're already doing something awesome.

Let’s build something fun and useful together!

## 🧠 Before You Start

Here are a few things to keep in mind before jumping in:

- 🏗 **This project is a work in progress.** Features may break, things might change, and some parts are still being figured out as I go.
- 📖 **Please read the README** to understand the vision, goals, and current progress.
- 🧪 **Tests and structure may be basic** (for now) — feel free to improve them!
- 🙋‍♂️ **If you're unsure about something, open an issue first.** I’d rather talk it out than reject a PR you worked hard on.
- 💬 **Feedback is welcome — even non-code stuff.** UX, naming, structure, suggestions — all good.

The goal is to build a system that works well, not just something that looks fancy. So whether you're contributing code, thoughts, or energy, you're part of that mission.


## 🛠️ How to Contribute

Here's the easiest way to get started with contributing:

### 1. Fork the Repository

Click the "Fork" button at the top right of this repo to create your own copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/your-username/pokemon-tcg-market-ph.git
cd pokemon-tcg-market-ph
```

### 3. Create a New Branch

Give your branch a name related to your work:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 4. Make Your Changes

Edit files, write code, improve docs — anything!

If you're adding a new feature or endpoint, try to:
- Keep functions short and readable
- Add comments for anything non-obvious
- Follow the current code style

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: add feature name here"
```

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Open a Pull Request

Go to the original repo and click **"Compare & pull request"**. Add a short description of what you did and why.

---

> If you're unsure about anything, it's totally okay. You can still open a draft PR or create an issue to ask for help or feedback before diving deep.


## ✨ Code Style & Guidelines

This project isn’t overly strict — but I do follow some basic principles to keep things clean and easy to maintain.

### 🔤 Naming & Structure

- Use **descriptive names** for functions, variables, and files — clarity over cleverness.
- Favor explicit names (`add_card_to_catalogue()`) over generic ones (`handle_data()`).
- Isolate logic where possible. Avoid mixing business logic with routes or models.
- If a function/module feels like it's doing too much, break it out into a helper or utility.

### 🧼 Formatting & Linting

- Python: Use **Black** for auto-formatting.
- Stick to **PEP8**, but don’t over-obsess — clean > perfect.
- Use **docstrings** for all non-trivial functions.

### 📁 Folder Structure (WIP, but evolving)

- `api/` – FastAPI routes and main app logic
- `core/` – business logic, OCR processing, pricing, etc.
- `db/` – database models and queries
- `client/` – React frontend (later)
- `tests/` – pytest tests

### ✅ Commits

Use conventional commits when possible:

```
feat: add webcam scanning endpoint
fix: handle empty card name bug
refactor: move OCR logic to separate module
docs: update README with new setup steps
```

### 🤝 Be Kind to Future You

Comment why something exists if it isn’t obvious. The goal isn’t fancy code — it’s **working systems you can maintain**.

## 🔄 Submitting a Pull Request

Before submitting a PR, please make sure you've:

- [ ] Followed the code style and formatting rules (run `black .` before commit)
- [ ] Written clear commit messages (use `feat:`, `fix:`, etc.)
- [ ] Added a helpful PR title and description
- [ ] Tested your changes locally (especially if it's backend logic)
- [ ] Commented any non-obvious logic

### 📋 PR Tips

- You can open a **draft PR** if you want early feedback or you're not 100% done.
- I review PRs when I can (usually within a few days).
- Let's be both open to feedback and real discussions — feel free to push back if something doesn’t make sense.

## 🐞 Reporting Issues

Found a bug, confusion point, or have a feature idea? Open an issue — it really helps!

When opening an issue:

- Use a **clear title**
- Describe what happened and what you expected
- If possible, include steps to reproduce
- Screenshots or code snippets are welcome
- Mark it as a `bug`, `feature`, or `question` if you can

No idea is too small. Even pointing out bad wording, confusing flows, or missing docs is helpful.

## 🙏 Acknowledgment & Review Flow

Thanks for taking the time to contribute!

Here’s what happens after you open a PR or issue:

- I’ll try to **review within a few days** (I'm currently a solo dev, so thanks for your patience!)
- I might leave comments or suggestions — feel free to discuss or challenge anything
- If everything looks good, I’ll merge it in and add your name to the credits 🙌

Every contribution — big or small — helps move this project forward.
