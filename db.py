from pymongo import MongoClient
from bson import json_util
from flask import Flask

app = Flask(__name__)

from . import db
client = db.init_db()

def init_db():
    client = MongoClient('mongodb://%s:%s@127.0.0.1' % ('mongouser', 'password'))
    client.tododb.todo.drop()
    client.tododb.todo.insert_many(
        [
            {"priority": "high",
            "title": "Get milk"},
            {"priority": "medium",
            "title": "Get gasoline"},
            {"priority": "low",
            "title": "Water plants"}
        ]
    )
    return client

@app.route("/todos")
def index():
    result = client.tododb.todo.find({})
    return json_util.dumps(list(result)), 200

@app.route("/todos/<priority>")
def get_by_priority_better(priority):
    result = client.tododb.todo.find({"priority": priority})
    result_list = list(result)
    if not result or len(result_list) < 1:
        return json_util.dumps(result_list), 404

    return json_util.dumps(result_list), 200

