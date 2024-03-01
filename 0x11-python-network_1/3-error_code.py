#!/usr/bin/python3
"""
Get request
handle exceptions, and show.
"""

import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
