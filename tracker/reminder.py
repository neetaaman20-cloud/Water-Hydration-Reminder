import time
import subprocess
from datetime import datetime
from tracker.logger import log_water
from config import REMINDER_INTERVAL_MINUTES, DAILY_GOAL_GLASSES

def send_mac_notification(title, message):
    """Send native Mac notification using osascript — works perfectly on M1"""
    script = f'display notification "{message}" with title "{title}" sound name "Drop"'
    subprocess.run(["osascript", "-e", script])

def start_reminder():
    glasses = 0
    print(f"\n✅ Reminders started! Every {REMINDER_INTERVAL_MINUTES} mins.")
    print("   Press CTRL+C to stop.\n")

    while glasses < DAILY_GOAL_GLASSES:
        now = datetime.now().strftime("%H:%M:%S")
        glasses += 1
        log_water(glasses)

        message = f"Glass {glasses}/{DAILY_GOAL_GLASSES} — Keep it up! 💪"
        send_mac_notification("💧 Time to Drink Water!", message)

        print(f"[{now}] 💧 Reminder sent! Glass {glasses}/{DAILY_GOAL_GLASSES}")

        if glasses < DAILY_GOAL_GLASSES:
            print(f"   ⏳ Next reminder in {REMINDER_INTERVAL_MINUTES} minutes...\n")
            time.sleep(REMINDER_INTERVAL_MINUTES * 60)

    print("\n🎉 You reached your daily water goal! Amazing!")
    send_mac_notification("🎉 Goal Reached!", "You drank all 8 glasses today! Great job!")
