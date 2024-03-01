#!/usr/bin/python3
"""
POST request with email passes as an arg
Usage:
    2-post_email.py URL email
sends a POST request and return the body decoded
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    body = {"email": sys.argv[2]}
    body = urllib.parse.urlencode(body).encode('ascii')
    req = urllib.request.Request(url=sys.argv[1], headers=headers,
                                 data=body, method="POST")
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode('UTF8'))
