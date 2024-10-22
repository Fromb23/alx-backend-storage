#!/usr/bin/env python3
"""
    update topics
"""


def update_topics(mongo_collection, name, topics):
    """
    return updated topics
    """
    filter_criteria = {"name": name}
    update_operation = {"$set": {"topics": topics}}
    return mongo_collection.update_many(filter_criteria, update_operation)
