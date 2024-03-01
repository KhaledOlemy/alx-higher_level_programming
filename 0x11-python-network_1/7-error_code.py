#!/usr/bin/python3
"""
get url response, handle if status is not 200
"""
import requests
import sys

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if resp.status_code < 400:
        print(resp.text)
    else:
        print("Error code: {resp.status_code}")
