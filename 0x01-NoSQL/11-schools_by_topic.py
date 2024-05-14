#!/usr/bin/env python3
"""This module constains one function"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.
    Args:
    mongo_collection (pymongo.collection.Collection):
        The pymongo collection object.
    topic (str):
        The topic to search.
    Returns:
    list: A list of school documents.
    """
    if not mongo_collection:
        return []
    documents = mongo_collection.find({"topics": topic})
    return [doc for doc in documents] if documents else []