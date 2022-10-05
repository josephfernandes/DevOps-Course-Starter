from flask import Flask , render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_login import LoginManager, login_required, login_user
import os, requests


from todo_app.data.to_do_item import ToDoItem
from todo_app.data.mongodb import show_cards, add_card, doing_card, done_card, delete_card
from todo_app.data.user import User
 

from todo_app.flask_config import Config
from todo_app.data.viewmodel import ViewModel

client_id='CLIENTID'
client_secret='CLIENTSECRET'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
       return redirect ('https://github.com/login/oauth/authorize?client_id='+ os.getenv(client_id)) 
     
    
    @login_manager.user_loader
    def load_user(user_id):
        print(user_id)
        pass # We will return to this later
    login_manager.init_app(app)
    
    @app.route('/login/callback')
    def login():
        code= request.args.get('code')
        access_token_url = 'https://github.com/login/oauth/access_token'
        payload = {
            'client_id': os.getenv(client_id),
            'client_secret': os.getenv(client_secret),
            'code': code,
        } 
        r = requests.post(access_token_url, json=payload, headers={'Accept': 'application/json'})
        access_token = r.json().get('access_token')
        print(access_token)
        reqUrl = "https://api.github.com/user"

        headersList = {
        "Accept": "*/*",
        "Authorization": f"Bearer {access_token}" 
        }

        response = requests.get(reqUrl, headers=headersList)

        response_json = response.json()

        print(response_json)

        user = User(response_json['id'])

        login_user(user)
        return redirect('/')


    @app.route('/')
    @login_required
    def home():
        to_do=show_cards()
        item_view_model = ViewModel(items=to_do)
        return render_template('index.html', to_do=to_do, view_model=item_view_model)

    @app.route('/newitem', methods= ["POST"])
    @login_required
    def new_item():
        item = request.form["title"]
        add_card(item)
        return redirect(url_for("home"))

    @app.route('/doingitem', methods= ["POST"])
    @login_required
    def to_doing_item():
        item = request.form["doing_item_form"]
        doing_card(item)
        return redirect(url_for("home"))

    @app.route("/done_card", methods=["POST"])
    @login_required
    def complete_item():
        item = request.form["done_card_form"]
        done_card(item)
        return redirect(url_for("home"))

    @app.route('/delete_card', methods=["POST"])
    @login_required
    def delete_item():
        item = request.form["delete_card"]
        delete_card(item)
        return redirect(url_for("home"))

    return app


        
 

