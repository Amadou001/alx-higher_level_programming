#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
# Display only body of a 200 status code response

URL="$1"

# Send a GET request and capture the response headers and body
response=$(curl -s -w "%{http_code}" "$URL")
body="${response%[0-9][0-9][0-9]}"
status_code="${response: -3}"

# Check if the status code is 200
if [ "$status_code" -eq 200 ]; then
  # Display the body of the response
  echo "$body"
fi
