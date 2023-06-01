from app import Blueprint, jsonify, request, json, app
from app.use_db import authorization
from authorization.hash import hash_password, check_password
import jwt
import datetime


authorization_blueprint = Blueprint('authorization', __name__)


@authorization_blueprint.route('/registration', methods=['POST'])
def registration():
    if request.method == 'POST':
        email = request.json['email']
        login = request.json['login']
        password = request.json['password']

        email_exist = authorization.check_email_exist(email)

        if email_exist[0] == 1:
            return jsonify({"error": "это почта уже существует"}), 403

        elif email_exist[0] == 0:
            login_exist = authorization.check_login_exist(login)

            if login_exist[0] == 1:
                return jsonify({"error": "этот логин уже существует"}), 403

            elif login_exist[0] == 0:

                hash_pass = hash_password(password)

                authorization.add_account_to_bd(login, email, hash_pass)

                token = jwt.encode({
                    'sub': email,
                    'iat': datetime.datetime.utcnow(),
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=5)
                }, app.config['SECRET_KEY'], algorithm="HS256")

                return jsonify(
                    {
                        'token': token,
                        'login': login,
                        'email': email
                    }
                )


@authorization_blueprint.route('/enter', methods=['POST'])
def enter():
    if request.method == 'POST':
        login = request.json['login']
        password = request.json['password']

        login_exist = authorization.check_login_exist(login)

        if login_exist[0] == 1:
            password_hash_form_bd = authorization.get_password_hash_from_bd(login)

            if check_password(password, password_hash_form_bd[0]):

                email = authorization.get_email(login)

                token = jwt.encode({
                    'sub': email[0],
                    'iat': datetime.datetime.utcnow(),
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=5)
                }, app.config['SECRET_KEY'], algorithm="HS256")

                return jsonify(
                    {
                        'token': token,
                        'login': login,
                        'email': email
                    }
                )

            else:
                return jsonify({"error": "неправильный пароль"}), 403

        else:
            return jsonify({"error": "неправильный логин"}), 403
