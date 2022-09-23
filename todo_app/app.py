from flask import Flask , render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_login import LoginManager

from todo_app.data.classes import to_do_item
from todo_app.data.mongodb import show_cards, add_card, doing_card, done_card, delete_card
 

from todo_app.flask_config import Config
from todo_app.data.viewmodel import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    login_manager = LoginManager()
    @login_manager.unauthorized_handler
    def unauthenticated():
        pass # Add logic to redirect to the GitHub OAuth flow when unauthenticated
    
    @login_manager.user_loader
    def load_user(user_id):
        pass # We will return to this later
    login_manager.init_app(app)
    

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

if __name__ == "__main__":
    create_app(create_app).run()
        
 

