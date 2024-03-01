#!/usr/bin/python3
"""
get url response, handle if status is not 200
"""
import requests
import sys

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if resp.status_code == 200:
        print(resp.text)
    else:
        print(resp.status_code)
