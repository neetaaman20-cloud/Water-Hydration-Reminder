import json
import os
from datetime import datetime
from config import GLASS_SIZE_ML, DAILY_GOAL_GLASSES

LOG_FILE = "data/log.json"

def log_water(glasses):
    today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")

    # Load existing data
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    # Update today's log
    if today not in data:
        data[today] = []

    data[today].append({
        "glass": glasses,
        "time": time_now,
        "ml": GLASS_SIZE_ML
    })

    # Save back
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_log():
    today = datetime.now().strftime("%Y-%m-%d")

    if not os.path.exists(LOG_FILE):
        print("\n📭 No log found. Start reminders first!")
        return

    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    if today not in data:
        print("\n📭 No entries for today yet.")
        return

    entries = data[today]
    total_ml = len(entries) * GLASS_SIZE_ML

    print(f"\n📊 Today's Water Log — {today}")
    print("=" * 40)
    for entry in entries:
        print(f"  Glass {entry['glass']} — {entry['time']} — {entry['ml']}ml")
    print("=" * 40)
    print(f"  Total: {len(entries)}/{DAILY_GOAL_GLASSES} glasses — {total_ml}ml")

    if len(entries) >= DAILY_GOAL_GLASSES:
        print("  🎉 Daily goal completed!")
    else:
        remaining = DAILY_GOAL_GLASSES - len(entries)
        print(f"  💪 {remaining} more glasses to go!")
