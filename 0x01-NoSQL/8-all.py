#!/usr/bin/env python3


"""
    list all docs in a collection
"""


def list_all(mongo_collection):
    """
    return the list in collection
    """
    mongo_list = []
    if mongo_collection is None:
        return mongo_list
    else:
        return mongo_list = list(mongo_collection.find())
