#!/usr/bin/python3
"""
get 10 commits of input user and repo passed as args
"""

import requests
import sys
if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10&page=1"
    url = url.format(sys.argv[2], sys.argv[1])
    try:
        resp = requests.get(url).json()
        for i in resp:
            print("{}: {}".format(i['sha'], i['commit']['author']['name']))
    except ValueError:
        print("Invalid Json")
