# 🍲 Flask Recipe App

A recipe search and bookmarking web app built with Flask and the Spoonacular API. Users can register, log in, search for recipes with dietary filters, view recipe details in modals, and save bookmarks for future reference.

---

## 🚀 Features

- 🔐 User registration & login (username-only for quick demo)
- 🔍 Search recipes using Spoonacular API with filters (diet, cuisine, intolerances)
- 📋 View recipe details in a Bootstrap modal
- ⭐ Save favorite recipes to your personal bookmark page
- ❌ Remove saved bookmarks
- 🎨 Clean responsive UI with Bootstrap
- 🔑 API keys and secrets stored securely in `.env`

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Flask-Login & SQLAlchemy
- Bootstrap 5
- SQLite (local DB)
- Spoonacular API

---

## 📦 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/recipe-app.git
cd recipe-app
```

### 2. Create a virtual environment & activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file
```
SECRET_KEY=your_secret_key_here
SPOONACULAR_API_KEY=your_spoonacular_api_key_here
```

### 5. Run the app
```bash
python run.py
```
Open your browser at `http://127.0.0.1:5000`

---

## 🔑 Demo Credentials

Use this account to quickly log in:
```
Username: demo
Password: demo123
```

---

## 📸 Screenshots
_Add screenshots of your UI here (login, search, modal, bookmarks)_

---

## 📄 License
MIT License — free to use and modify!
