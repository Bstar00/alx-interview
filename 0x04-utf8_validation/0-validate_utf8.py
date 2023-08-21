#!/usr/bin/python3
""" This script checks if a sequence of integers
    represents valid UTF-8 encoded data.
"""


def validUTF8(data):
    """ Check if the given data is a valid UTF-8 encoding. """
    try:
        masked_data = [n & 255 for n in data]
        bytes(masked_data).decode("UTF-8")
        return True
    except Exception:
        return False
