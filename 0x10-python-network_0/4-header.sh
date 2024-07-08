#!/bin/bash
# takes in a URL as an arg, sends a GET request to URL, and displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
