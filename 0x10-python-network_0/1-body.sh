#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
# Display only body of a 200 status code response
# Check if a URL was provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL="$1"

# Send a GET request and capture the response headers and body
response=$(curl -sL -w "%{http_code}" -o - "$URL")
body="${response%???}"
status_code="${response: -3}"

# Check if the status code is 200
if [ "$status_code" -eq 200 ]; then
  # Display the body of the response
  echo "$body"
fi
