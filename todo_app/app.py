from flask import Flask , render_template, request, redirect, url_for

from todo_app.data.trello_items import  show_cards, add_card, doing_card

from todo_app.flask_config import Config



app = Flask(__name__)
app.config.from_object(Config())

@app.route('/', methods= ["GET"] )
def home():
  trello_list = show_cards()
  to_do = []
  for list  in trello_list:
    for card in list ['cards']:
      to_do.append(card)
      return render_template('index.html', to_do=to_do)

@app.route('/newitem', methods= ["POST"])
def new_item():
    item = request.form["new_item_form"]
    add_card(item)
    return redirect(url_for("home"))

@app.route('/doingitem', methods= ["POST"])
def to_doing_item():
    item = request.form["doing_item_form"]
    doing_card(item)
    return redirect(url_for("home"))