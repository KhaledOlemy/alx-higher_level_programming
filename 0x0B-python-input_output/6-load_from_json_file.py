#!/usr/bin/python3
""" LOADING FROM A JSON FILE """
import json


def load_from_json_file(filename):
    """ load a JSON """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.loads(f.read())
