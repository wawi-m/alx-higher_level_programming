#!/usr/bin/python3
"""
This module fetches the status from https://alx-intranet.hbtn.io/status
using the requests package and displays the body of the response.
"""

import requests

def fetch_status():

    """
    Fetches the status from the given URL and prints the response
    in a formatted manner.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    body = response.text
    
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body))

if __name__ == "__main__":

    fetch_status()
