import pymongo
from .config import username, password, host, db_name, collection_name

URI = f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority"
client = pymongo.MongoClient(URI)
db = client[db_name]
coll = db[collection_name]


def get_timetables(**kwargs):
    timetables = list(coll.find({k: v for k, v in kwargs.items() if v}))
    return [{"public": t["public"], "name": t["name"], "timetable": t["timetable"]} for t in timetables]


def create_timetable(email, public, name, timetable):
    if coll.count_documents({"email": email, "name": name}) > 0:
        return -1
    oid = coll.insert_one({"email": email, "public": public, "name": name, "timetable": timetable})
    return 1


def delete_timetable(**kwargs):
    d = coll.delete_many({k: v for k, v in kwargs.items() if v})
    return d.delete_count


def update_timetable(filter_, update):
    res = coll.update_many(filter_, {"$set": update})
    return res.modified_count
