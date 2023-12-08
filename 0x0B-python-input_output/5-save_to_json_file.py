#!/usr/bin/python3
""" WRITING A JSON FILE """
import json


def save_to_json_file(my_obj, filename):
    """ write a JSON file """
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
