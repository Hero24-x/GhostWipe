from utils import banner
from modules import linux_cleaner, termux_cleaner, log_poisoner, auto_scheduler

def main():
    banner.show()
    print("1. Full Clean")
    print("2. Termux Clean")
    print("3. Add Fake Logs (Poison)")
    print("4. Schedule Auto-Wipe")
    print("5. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        linux_cleaner.full_clean()
    elif choice == "2":
        termux_cleaner.termux_clean()
    elif choice == "3":
        log_poisoner.poison_logs()
    elif choice == "4":
        auto_scheduler.setup_cron()
    else:
        print("👋 Exiting GhostWipe...")

if __name__ == "__main__":
    main()
  
