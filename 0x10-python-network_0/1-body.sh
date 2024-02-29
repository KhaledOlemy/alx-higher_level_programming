#!/bin/bash
# GET only the body of a 200 page
code=$(curl -sIL $1 | grep -i HTTP/ | awk '{print $2}' | tail -n1)
if [ $code -eq 200 ]; then
    curl -sL $1;
fi
