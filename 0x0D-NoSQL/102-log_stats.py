#!/usr/bin/env python3

""" that provides some stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


def log_stats(mongo_collection):
    """ that provides some stats about Nginx logs stored in MongoDB """

    print("{} logs".format(mongo_collection.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print("\tmethod {}: {}".format(
            method, mongo_collection.count_documents({"method": method})))

    print("{} status check".format(
        mongo_collection.count_documents({"path": "/status"})))

    print("IPs:")
    ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.01:27017')
    nginx = client.logs.nginx
    log_stats(nginx)
