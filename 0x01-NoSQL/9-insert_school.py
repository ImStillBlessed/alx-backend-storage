#!/usr/bin/env python3
"""This module constains one function"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    Args:
    mongo_collection (pymongo.collection.Collection):
        The pymongo collection object.
    kwargs (dict):
        The dictionary with the document data.
    Returns:
    str: The new _id.
    """
    if not mongo_collection:
        return None
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
