#!/usr/bin/env python3
"""This module constains one function"""
from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    Returns:
        None
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: 0 for method in methods}

    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})

    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")

    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
