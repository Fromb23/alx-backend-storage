#!/usr/bin/env python3
"""
    insert school
"""


def insert_school(mongo_collection, **kwargs):
    """
    return the new id
    """
    insert = mongo_collection.insert_one(kwargs)
    return insert.inserted_id
