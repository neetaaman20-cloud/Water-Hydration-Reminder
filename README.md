# 💧 Water & Hydration Reminder App

> *Designed & Developed by **Anugrah Singh***

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-macOS%20M1-000000?style=for-the-badge&logo=apple&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

A Mac-native Python wellness app that reminds you to drink water,
tracks your daily hydration, and sends real Mac notifications —
because your health matters. 💪

---

## 🧑‍💻 Developer

| | |
|---|---|
| **Name** | Anugrah Singh |
| **GitHub** | [@neetaaman20-cloud](https://github.com/neetaaman20-cloud) |
| **Platform** | MacBook Air M1 |
| **Language** | Python 3.8+ |

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| 🐍 Python 3.8+ | Core programming language |
| 📦 JSON | Local data storage for hydration logs |
| 🔔 osascript | Native macOS notification system |
| 🕐 time module | Interval-based reminder scheduling |
| 🗂️ os module | File system & environment handling |
| 📁 dotenv | Environment configuration |

---

## 📁 Project Structure

Water-Hydration-Reminder/
│
├── tracker/
│   ├── init.py       # Package initializer
│   ├── reminder.py       # Reminder logic & Mac notifications
│   └── logger.py         # Water intake logging system
│
├── data/
│   └── log.json          # Daily hydration data (auto-generated)
│
├── main.py               # App entry point
├── config.py             # User configuration settings
├── requirements.txt      # Dependencies
└── README.md             # Project documentation


---

## ✨ Features

- 🔔 **Native Mac Notifications** — Real macOS popups with sound
- 💧 **Smart Reminders** — Customizable interval reminders
- 📊 **Daily Log Tracker** — Tracks every glass with timestamp
- 💾 **JSON Storage** — Saves hydration history locally
- 📈 **Progress Report** — Shows daily goal completion
- ⚙️ **Fully Customizable** — Edit goals, intervals & glass size

---

## ⚙️ Configuration (`config.py`)

```python
REMINDER_INTERVAL_MINUTES = 30   # How often to remind you
DAILY_GOAL_GLASSES = 8           # Your daily water goal
GLASS_SIZE_ML = 250              # Size of each glass in ml

💻 Requirements
	∙	MacBook (M1 or any Mac)
	∙	Python 3.8+
	∙	No paid APIs needed!
	∙	No external libraries needed!

# Clone the repository
git clone https://github.com/neetaaman20-cloud/Water-Hydration-Reminder.git

# Go into the project folder
cd Water-Hydration-Reminder

# Run the app
python3 main.py


📱 App Menu

==========================================
      💧 Water & Hydration Reminder App
==========================================

1. Start Hydration Reminders
2. View Today's Water Log
3. Exit

