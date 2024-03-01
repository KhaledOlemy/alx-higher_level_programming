#!/usr/bin/python3
"""
use requests to fetch 'https://alx-intranet.hbtn.io/status'
get body content and type
"""
import requests

if __name__ == "__main__":
    body = requests.get('https://alx-intranet.hbtn.io/status').text
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
