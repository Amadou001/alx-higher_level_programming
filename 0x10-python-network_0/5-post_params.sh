#!/bin/bash
# Bash script that send a post request to url
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
