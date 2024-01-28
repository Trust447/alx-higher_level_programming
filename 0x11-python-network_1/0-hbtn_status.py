#!/usr/bin/python3

import urllib.request
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()

    '''Convert the response content to UTF-8 string'''
    utf8_content = body.decode('utf-8')

    print('Body response:')
    print("     - type: {}".format(type(body)))
    print("     - content: {}".format(body))
    print("     - utf8 content: {}".format(utf8_content))
