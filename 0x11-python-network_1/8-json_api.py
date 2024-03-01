#!/usr/bin/python3
"""
search API and find queries
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = f"q={q}"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    try:
        resp = requests.post(url, data=data, headers=headers)
        if resp.json():
            print(f"[{resp.json().get('id')}] {resp.json().get('name')}")
        else:
            print("No result")
    except:
        print("Not a valid JSON")
