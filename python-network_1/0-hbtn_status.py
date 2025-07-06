#!/usr/bin/python3
"""
This module fetches the status of a specific URL using urllib
and prints out the type and content of the response in a formatted way.
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
        fetch_page = response.read()

    print("Body response:")
    print("\t- type:", type(fetch_page))
    print("\t- content:", fetch_page)
    print("\t- utf8 content:", fetch_page.decode('utf-8'))
