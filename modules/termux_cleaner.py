import os

def termux_clean():
    termux_paths = [
        "~/.bash_history",
        "~/.zsh_history",
        "~/.termux/termux.properties",
        "~/.shortcuts"
    ]
    with open("results/wipe_report.txt", "a") as log:
        for path in termux_paths:
            full_path = os.path.expanduser(path)
            if os.path.exists(full_path):
                try:
                    open(full_path, "w").close()
                    log.write(f"Termux wiped: {full_path}\n")
                    print(f"[+] Wiped {full_path}")
                except Exception as e:
                    print(f"[-] Error wiping {full_path}: {e}")
                  
