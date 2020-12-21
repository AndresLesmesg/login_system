from flask import session

from . import views

from app.models.session import Session
from app.models.auth import Auth
from app.models.user import User


@views.route('/sign_up')
def login():
    users = User.get_user_all()
    auth = Auth.get_by_id(1)
    login = Session.add_session()
    session['users'] = users
    session['auth'] = auth
    session['session'] = login
    print(session)
    return "sign up"
