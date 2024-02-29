#!/bin/bash
# GET only the body of a 200 page
code=$(curl -sI $1 | grep -i HTTP | awk 'NR==1{print $2}')
if [ $code -eq 200 ]; then
    curl -s $1;
fi
