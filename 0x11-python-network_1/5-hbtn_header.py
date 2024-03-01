#!/usr/bin/python3
"""
use requests and sys to get the header value of 'X-Request-Id'
for the site passed as an argument
"""
import requests
import sys
if __name__ == "__main__":
    resp = requests.get(sys.argv[1]).headers.get('X-Request-Id')
    print(resp)
