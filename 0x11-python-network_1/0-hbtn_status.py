#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

URL = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(URL) as response:
    data = response.read()
    text = data.decode('utf-8')
    print("Body response:")
    print("\t- {}".format(text))
