#!/bin/bash
# get status code only
curl -sLI olemy.tech/redirect_me | grep HTTP/ | awk '{print $2}' | tail -n1
