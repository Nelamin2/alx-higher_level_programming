#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
response=$(mktemp)
curl -sX GET -o "$response" "$1" -L
size=$(wc -c < "$response")
echo "Size of response body: $size bytes"
rm "$response"

