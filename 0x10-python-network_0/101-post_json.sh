#!/bin/bash
# POST request with JSON payload
curl -sX POST -H "Content-Type: application/json" -d @$2 $1
