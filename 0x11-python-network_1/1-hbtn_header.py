#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends
a request to the URL and displays the value of
the X-Request-Id variable found in the header
of the response."""
import urllib.request
import sys

if len(sys.argv) != 2:
    sys.exit(1)

URL = sys.argv[1]

if __name__ == "__main__":
    url = urllib.request.Request(URL)
    with urllib.request.urlopen(url) as Response:
        Id = Response.headers.get("X-Request-Id")
        print("{}".format(Id))
