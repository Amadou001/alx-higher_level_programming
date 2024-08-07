#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

URL = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(URL) as response:
    data = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode('utf-8')))
