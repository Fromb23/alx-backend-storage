#!/usr/bin/env python3
"""
    Script to provide stats about Nginx logs in MongoDB.
    """
from pymongo import MongoClient


def get_nginx_stats():
    """
    Fetch and display statistics
    from the Nginx logs collection.
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    nginx_collection = db["nginx"]

    total_logs = nginx_collection.count_documents({})

    # count by http methods
    methods_count = {
            "GET": nginx_collection.count_documents({"method": "GET"}),
            "PUT": nginx_collection.count_documents({"method": "PUT"}),
            "POST": nginx_collection.count_documents({"method": "POST"}),
            "PATCH": nginx_collection.count_documents({"method": "PATCH"}),
            "DELETE": nginx_collection.count_documents({"method": "DELETE"})
            }

    get_status_count = nginx_collection.count_documents(
                        {"method": "GET", "path": "/status"}
                        )

    # Display the results
    print(f"{total_logs} logs")
    print("Methods:")
    print(f"\tGET: {methods_count['GET']}")
    print(f"\tPOST: {methods_count['POST']}")
    print(f"\tPUT: {methods_count['PUT']}")
    print(f"\tPATCH: {methods_count['PATCH']}")
    print(f"\tDELETE: {methods_count['DELETE']}")
    print(f"GET /status: {get_status_count}")


if __name__ == "__main__":
    get_nginx_stats()
