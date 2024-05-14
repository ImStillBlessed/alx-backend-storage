#!/usr/bin/env python3
"""This module constains one function"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.
    Args:
    mongo_collection (pymongo.collection.Collection):
        The pymongo collection object.
    name (str):
        The school name to update.
    topics (list):
        The list of topics approached in the school.
    Returns:
    int: The number of documents updated.
    """
    if not mongo_collection:
        return 0
    updated = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return updated.modified_count
