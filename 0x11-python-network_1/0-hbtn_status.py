#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()

    '''Convert the response content to UTF-8 string'''
    utf8_content = body.decode('utf-8')

    print('Body response:')
    print("     - type: {}".format(type(body)))
    print("     - content: {}".format(body))
    print("     - utf8 content: {}".format(utf8_content))
