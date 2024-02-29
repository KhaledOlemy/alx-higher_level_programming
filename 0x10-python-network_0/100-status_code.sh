#!/bin/bash
# get status code only
curl https://www.google.com --silent --output /dev/null --write-out "%{http_code}"
