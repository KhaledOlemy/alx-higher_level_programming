#!/bin/bash
# POST request with JSON payload
curl -X POST -H "Content-Type: application/json" -d @$2 $1
