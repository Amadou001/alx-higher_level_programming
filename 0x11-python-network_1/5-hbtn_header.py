#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
You must use the packages requests and sys
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
