# 🧼 GhostWipe – Leave No Trace. Ever.

> ⚔️ A stealth-class log and history eraser for Linux & Termux.  
> 🕶️ Clean up your bash/zsh history, system logs, termux traces, and even plant fake logs to stay steps ahead.

---

## 👤 Author

**👨‍💻 Developed by:** [Shibnath Hansda](https://github.com/hansdatechs)  
🎥 **YouTube Channel:** [HansdaTechs](https://www.youtube.com/@HansdaTechs)

---

## 🎯 Key Features

✅ **Full Log Erasure** – Clean system logs, shell histories, wtmp/btmp, and cron artifacts  
📱 **Termux Support** – Clears `.bash_history`, `.shortcuts`, `termux.properties` and more  
🧪 **Log Poisoning** – Inject realistic fake commands (like `nano`, `ping`, `apt update`)  
📅 **Auto-Wipe Scheduler** – Set daily/weekly ghost cleanups via cron/Termux boot  
📋 **Wipe Report Logging** – Every wipe saved in `results/wipe_report.txt`  
🧠 **Smart Shell Detection** – Detects OS + shell and adjusts accordingly

---

## 📦 Installation

### 🔧 Requirements

- Python 3.8+
- pip
- Linux (Kali/Ubuntu/Parrot) or Android (via Termux)

### 🛠️ Setup

```bash
git clone https://github.com/hansdatechs/ghostwipe.git
cd ghostwipe
pip install -r requirements.txt

## 🚀 Usage
python3 ghostwipe.py
