#!/usr/bin/env python3
"""This module constains one function"""
def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    Args:
    mongo_collection (pymongo.collection.Collection):
        The pymongo collection object.
    Returns:
    list: A list of documents in the collection.
        Returns an empty list if no documents found.
    """
    if not mongo_collection:
        return []
    documents = list(mongo_collection.find())
    return documents if documents else []
