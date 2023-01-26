from flask import Flask , render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect

from todo_app.data.classes import to_do_item
from todo_app.data.mongodb import show_cards, add_card, doing_card, done_card, delete_card
 

from todo_app.flask_config import Config
from todo_app.data.viewmodel import ViewModel
import logging

from loggly.handlers import HTTPSHandler
from logging import Formatter


app = Flask(__name__)
app.config.from_object(Config())
if app.config['LOGGLY_TOKEN'] is not None:
    handler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{app.config["LOGGLY_TOKEN"]}/tag/todo-app')
    handler.setFormatter(Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
    )
    app.logger.addHandler(handler)
app.logger.info('This a debug message')
logging.warning('This an info message')
logging.error('This an error message')
logging.critical('This a criticl message')

@app.route('/' )
def home():
  to_do=show_cards()
  item_view_model = ViewModel(items=to_do)
  return render_template('index.html', to_do=to_do, view_model=item_view_model)

@app.route('/newitem', methods= ["POST"])
def new_item():
    item = request.form["title"]
    add_card(item)
    app.logger.info(f"Item {item} new item was added")
    return redirect(url_for("home"))

@app.route('/doingitem', methods= ["POST"])
def to_doing_item():
    item = request.form["doing_item_form"]
    doing_card(item)
    app.logger.info(f"Item {item} was moved to doing")
    return redirect(url_for("home"))

@app.route("/done_card", methods=["POST"])
def complete_item():
    item = request.form["done_card_form"]
    done_card(item)
    app.logger.info(f"Item {item} was moved to done")
    return redirect(url_for("home"))

@app.route('/delete_card', methods=["POST"])
def delete_item():
    item = request.form["delete_card"]
    delete_card(item)
    app.logger.info(f"Item {item} was deleted")
    return redirect(url_for("home"))
    
 

