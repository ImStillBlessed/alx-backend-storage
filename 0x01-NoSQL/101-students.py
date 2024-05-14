#!/usr/bin/env python3
"""This module constains one function"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
