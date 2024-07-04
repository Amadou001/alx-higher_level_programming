#!/bin/bash
# Bash script that takes in a URL, sends a request to that UR
URL="$1"
curl -sX DELETE "$URL"
