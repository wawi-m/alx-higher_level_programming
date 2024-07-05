import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        x_request_id = dict(headers).get('X-Request-Id')

    print(x_request_id)
