#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
"""
import urllib.request
import sys


if __name__ == "__main__":
    URL = sys.argv[1]

    url = urllib.request.Request(URL)
    with urllib.request.urlopen(url) as Response:
        print(dict(Response.headers).get("X-Request-Id"))
