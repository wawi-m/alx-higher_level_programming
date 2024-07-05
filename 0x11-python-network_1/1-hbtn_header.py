#!/usr/bin/python3
import urllib.request
import sys


def fetch_x_request_id(url):

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)
            else:
                print("No X-Request-Id found in the response headers.")
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
