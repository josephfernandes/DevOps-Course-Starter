import pymongo
from todo_app.data.classes import to_do_item
from pymongo import MongoClient
from bson import ObjectId 
import os

key = os.environ.get('CONNECTION_STRING')

client = MongoClient(f"{key}") #PRIMARY CONNECTION STRING
db = client.todo_app    #Select the database
todos = db.todo_tasks

def show_cards():
    reqUrl = f"https://{key}.documents.azure.com"
    parameters = { 
        "key": key,
        "token": token, 
        "cards": "open"
    }
    return requests.get(reqUrl, data=parameters).json()

def add_card(name):
    key = os.environ.get('CONNECTION_STRING')
    print(key)
    client = MongoClient(f"{key}") #PRIMARY CONNECTION STRING
    db = client.todo_app    #Select the database
    todos = db.todo_tasks
    card = { 
        "status": "to_do", 
        "name" : name 
    }
    card_id = todos.insert_one(card).inserted_id

def doing_card(id):
    reqUrl= f"https://api.trello.com/1/cards/{id}"
    parameters = { 
        "key": key, 
        "token": token,
        "idList":doing,
        
        "id": id
    }
    return requests.put(reqUrl, data=parameters)

def done_card(id):
    reqUrl= f"https://api.trello.com/1/cards/{id}"
    parameters = { 
        "key": key, 
        "token": token,
        "idList":done,
        
        "id": id
    }
    return requests.put(reqUrl, data=parameters)


def delete_card(id):
    reqUrl= f"https://api.trello.com/1/cards/{id}"
    parameters = { 
        "key": key, 
        "token": token,
        
    }
    return requests.request("DELETE", reqUrl, data=parameters).raise_for_status()

