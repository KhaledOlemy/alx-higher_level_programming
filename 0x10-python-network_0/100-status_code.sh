#!/bin/bash
# get status code only
curl $1 --silent --output /dev/null --write-out "%{http_code}"
