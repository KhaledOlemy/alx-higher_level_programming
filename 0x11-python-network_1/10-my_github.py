#!/usr/bin/python3
"""
get id of github user using HTTPBasicAuth, even it was easier through
calling this IP without the auth or pass/token with this API query:
https://api.github.com/users/{sys.argv[1]}
"""
import sys
import requests

if __name__ == "__main__":
    basicAuth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    resp = requests.get("https://api.github.com/user", auth=basicAuth)
    print(resp.json().get('id'))
