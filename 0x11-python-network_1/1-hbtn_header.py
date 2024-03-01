#!/usr/bin/python3
from urllib import request
import sys
with request.urlopen(sys.argv[1]) as resp:
    print(resp.getheader('X-Request-Id'))
