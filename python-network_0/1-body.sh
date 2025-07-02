#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
r=$(curl -s -L -w "%{http_code}" "$1"); s=${r: -3}; [[ $s == 200 ]] && echo -n "${r:: -3}"
