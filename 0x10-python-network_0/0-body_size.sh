#!/bin/bash
# curl body size
SIZE=$(curl -s -o /dev/null -w '%{size_download}' "$1")
