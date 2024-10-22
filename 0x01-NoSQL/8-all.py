#!/usr/bin/env python3
"""
    list all docs in a collection
"""


def list_all(mongo_collection):
    """
    return the list in collection
    """
    return list(mongo_collection.find())
