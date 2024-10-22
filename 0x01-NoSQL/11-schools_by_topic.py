#!/usr/bin/env python3
"""
    find topic in topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    return list of topic found
    """
    filter_criteria = {"topics": topic}

    return list(mongo_collection.find(filter_criteria))
