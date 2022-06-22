import os, requests, json
from todo_app.data.classes import to_do_item

key = os.environ.get('API_KEY')
token = os.environ.get('API_TOKEN')
board = os.environ.get('BOARD')
to_do = os.environ.get('TO_DO')
doing = os.environ.get('DOING')
done = os.environ.get('Done')
idl1 = os.environ.get('IdList1')
idl2 = os.environ.get('IdList2')
idl3 = os.environ.get('IdList3')

def show_cards():
    reqUrl = f"https://api.trello.com/1/boards/{board}/lists"
    parameters = { 
        "key": key,
        "token": token, 
        "cards": "open"
    }
    return requests.get(reqUrl, data=parameters).json()

def add_card(name):
    reqUrl= "https://api.trello.com/1/cards"
    parameters = { 
        "key": key, 
        "token": token, 
        # "idList": to_do,
    
        "idList":idl1,
        "name" : name 
    }
    return requests.post(reqUrl, data=parameters)

def doing_card(id):
    reqUrl= f"https://api.trello.com/1/cards/{id}"
    parameters = { 
        "key": key, 
        "token": token,
        "idList":idl2,
        # "idList": doing,
        "id": id
    }
    return requests.put(reqUrl, data=parameters)

def done_card(id):
    reqUrl= f"https://api.trello.com/1/cards/{id}"
    parameters = { 
        "key": key, 
        "token": token,
        "idList":idl3,
        # "idList": done,
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

