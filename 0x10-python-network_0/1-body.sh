#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
BODY=$(curl -Ls -w "%{http_code}" "$1" -o temp_body); [ "$BODY" -eq 200 ] && cat temp_body; rm -f temp_body
