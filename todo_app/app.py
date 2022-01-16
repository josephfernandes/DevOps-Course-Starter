from flask import Flask , render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config



app = Flask(__name__)
app.config.from_object(Config())

@app.route('/' )
def home():
    return render_template('index.html', get_items= get_items)

@app.route('/newitem', methods= ["POST"])
def new_item():
    item = request.form["title"]
    add_item(item)
    return redirect(url_for("home"))


