#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
echo '[ "$(curl -s -o -I -w '%{http_code}' "$1")" -eq 200 ] && curl -s "$1"'
