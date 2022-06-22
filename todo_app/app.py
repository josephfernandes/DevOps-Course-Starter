from flask import Flask , render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect

from todo_app.data.classes import to_do_item
from todo_app.data.trello_items import  show_cards, add_card, doing_card, done_card
 

from todo_app.flask_config import Config



app = Flask(__name__)
app.config.from_object(Config())

@app.route('/' )
def home():

  trello_list = show_cards()
  to_do = []
  for list  in trello_list:
    for card in list ['cards']:
      id=card ['id']
      title=card['name']
      status=list['name']
      item=to_do_item(id, title, status)
      to_do.append(item)
  return render_template('index.html', to_do=to_do)

   

@app.route('/newitem', methods= ["POST"])
def new_item():
  

    item = request.form["title"]

    add_card(item)
    return redirect(url_for("home"))

@app.route('/doingitem', methods= ["POST"])
def to_doing_item():
    item = request.form["doing_item_form"]
    doing_card(item)
    return redirect(url_for("home"))

@app.route("/done_card", methods=["POST"])
def complete_item():
    item = request.form["done_card_form"]
    done_card(item)
    return redirect(url_for("home"))

@app.route('/delete_card', methods=["POST"])
def delete_card():
    item = request.form["delete_card_form"]
    delete_card(item)
    return redirect(url_for("home"))
    
 

