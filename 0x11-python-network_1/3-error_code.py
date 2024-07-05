#!/usr/bin/python3

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000"

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
