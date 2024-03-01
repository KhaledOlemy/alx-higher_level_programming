#!/usr/bin/python3
from urllib import request
with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    resp = resp.read()
    print('Body response:')
    print('\t- type: {}'.format(type(resp)))
    print('\t- content: {}'.format(resp))
    print('\t- utf8 content: {}'.format(resp.encode('UTF8')))
