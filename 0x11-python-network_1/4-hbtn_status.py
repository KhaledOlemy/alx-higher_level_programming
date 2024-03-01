#!/usr/bin/python3
"""
use requests to fetch 'https://alx-intranet.hbtn.io/status'
get body content and type
"""
import requests

body = requests.get('https://alx-intranet.hbtn.io/status').text
print('Body response:')
print('\t- type: {}'.format(type(body)))
print('\t- content: {}'.format(body))
