#!/bin/bash
# curl body size
echo "Size of the body of the response: $(curl -s -o /dev/null -w '%{size_download}' "$1") bytes"
