def poison_logs():
    fake_logs = [
        "sudo apt install cowsay",
        "cd ~/Downloads",
        "ping google.com",
        "nano my_diary.txt"
    ]
    bash_history = os.path.expanduser("~/.bash_history")
    with open(bash_history, "a") as bh:
        for log in fake_logs:
            bh.write(f"{log}\n")
    print("[+] Added fake commands to bash_history.")
  
