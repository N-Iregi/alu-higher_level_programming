#!/usr/bin/python3
# fetches https://alu-intranet.hbtn.io/status using urllib

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
        fetch_page = response.read()

    print("Body Response:")
    print("\t- type:", type(fetch_page))
    print("\t- content:", fetch_page)
    print("\t- utf8 content:", fetch_page.decode('utf-8'))
