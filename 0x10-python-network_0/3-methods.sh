#!/bin/bash
# Bash script that takes in a URL, and display all htpp methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
