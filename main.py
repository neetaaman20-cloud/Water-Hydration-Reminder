from tracker.reminder import start_reminder
from tracker.logger import show_log

def main():
    print("=" * 45)
    print("     💧 Water & Hydration Reminder App")
    print("=" * 45)
    print("\n1. Start Hydration Reminders")
    print("2. View Today's Water Log")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == "1":
        start_reminder()
    elif choice == "2":
        show_log()
    elif choice == "3":
        print("\n👋 Stay hydrated! Goodbye!")
    else:
        print("\n❌ Invalid choice. Try again.")
        main()

if __name__ == "__main__":
    main()
