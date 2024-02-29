#!/usr/bin/env bash
# get Content-Length of a page
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
