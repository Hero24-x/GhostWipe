import os

def setup_cron():
    cron_job = "@daily python3 ~/ghostwipe/ghostwipe.py --auto"
    os.system(f'(crontab -l; echo "{cron_job}") | crontab -')
    print("[+] Auto-wipe scheduled daily via cron.")
  
