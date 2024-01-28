#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
"""
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
