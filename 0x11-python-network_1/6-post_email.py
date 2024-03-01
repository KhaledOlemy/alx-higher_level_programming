#!/usr/bin/python3
"""
POST request with email data, and return response
"""
import requests
import sys

if __name__ == "__main__":
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    body = f"email={sys.argv[2]}"
    resp = requests.post(sys.argv[1], headers=headers, data=body)
    print(resp.text)
