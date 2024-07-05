#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
"""

import urllib.request
import sys

URL = sys.argv[1]
with urllib.request.urlopen(URL) as response:
    x_Resquest_id = response.getheader('X-Request-Id')
    print(x_Resquest_id)
