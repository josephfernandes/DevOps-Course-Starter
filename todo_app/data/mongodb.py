from todo_app.data.to_do_item import ToDoItem
from pymongo import MongoClient
from bson import ObjectId 
import os

key = os.environ.get('CONNECTION_STRING')

client = MongoClient(key) #PRIMARY CONNECTION STRING
db = client.todo_app    #Select the database
todos = db.todo_tasks



def show_cards():
    tasks=[]
    for task in todos.find():
        tasks.append(ToDoItem(id=task["_id"], title=task["title"], status=task["status"]))
    return tasks
    
def add_card(name):
    key = os.environ.get('CONNECTION_STRING')
    
    card = { 
        "status": "To-Do", 
        "title": name
    }
    card_id = todos.insert_one(card).inserted_id

def doing_card(id):
    myquery = { "_id":ObjectId(id) }
    newvalues = { "$set":{ "status": "Doing" } }
    todos.update_one( myquery, newvalues)
    

def done_card(id):
    myquery = { "_id":ObjectId(id) }
    newvalues = { "$set":{ "status": "Done" } }
    todos.update_one( myquery, newvalues)
    


def delete_card(id):
    myquery = { "_id":ObjectId(id) }
    todos.delete_one( myquery)
    

