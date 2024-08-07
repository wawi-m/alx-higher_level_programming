#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8).
It handles urllib.error.HTTPError exceptions and prints the error code if an exception occurs.
"""
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
