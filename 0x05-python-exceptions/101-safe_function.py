#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        out = fct(*args)
        return out
    except Exception as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return None
