#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence or sentence == "":
        return 0, sentence[0]
    return len(sentence), sentence[0]
