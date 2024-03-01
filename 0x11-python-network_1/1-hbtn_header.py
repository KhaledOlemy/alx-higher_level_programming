#!/usr/bin/python3
"""
Retrieve 'X-Request-Id' value in the response headers
found in the request to the url passed as an arg
"""
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.getheader('X-Request-Id'))
