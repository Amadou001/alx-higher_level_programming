#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


if __name__=="__main__":
    import urllib
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = {
        'email': email
    }

    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url, data=encoded_data, method='POST')

    with urllib.request.urlopen(request) as response:
        response_data = response.read()
        print(response_data.decode('utf-8'))
