from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from config import Config
from flask_mysqldb import MySQL
import MySQLdb.cursors
from hash import check_password, hash_password
import bcrypt
import jwt
import datetime
from functools import wraps


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
mysql = MySQL(app)


def call(quarry, *args, commit, fetchall):

    cur = mysql.connection.cursor()

    cur.execute(quarry, *args)

    if commit:
        cur.close()

        mysql.connection.commit()

        result_of_quarry = None

    else:

        if fetchall:
            result_of_quarry = cur.fetchall()
            cur.close()
        else:
            result_of_quarry = cur.fetchone()
            cur.close()

    return result_of_quarry


@app.route('/', methods=['GET'])
def index():
    return "hello world"


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }

        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            email = data['sub']

            email_exist = call('select exists '
                               '(select * from person where email_per = %s)', [email], commit=False, fetchall=False)

            if email_exist[0] == 0:
                    raise RuntimeError('User not found')

            login = call('select login_per from person where email_per = %s', [email], commit=False, fetchall=False)
            return f(login[0], *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify


@app.route('/records', methods=['GET'])
@token_required
def show_records(login):

    id_per = call('select id_per from person where login_per = %s', [login], commit=False, fetchall=False)
    records = call('select * from records where id_per = %s', [id_per[0]], commit=False, fetchall=True)

    json_records = []
    for record in records:
        json_records.append({
            "id": record[0],
            "id_per": record[1],
            "record": record[2]
        })

    return jsonify({
        "records": json_records
    })


@app.route('/add_record', methods=['POST'])
@token_required
def add_record(login):
    if request.method == "POST":
        record = request.json['record']
        id_per = call('select id_per from person where login_per = %s', [login], commit=False, fetchall=False)

        call('insert into records(id_per, record) values (%s, %s)', [id_per[0], record], commit=True, fetchall=False)

        return "record is add"


@app.route('/registration', methods=['POST'])
def registration():
    if request.method == 'POST':
        email = request.json['email']
        login = request.json['login']
        password = request.json['password']

        email_exist = call('select exists '
                     '(select * from person where email_per = %s)', [email], commit=False, fetchall=False)

        if email_exist[0] == 1:
            return jsonify({"error": "это почта уже существует"}), 403


        elif email_exist[0] == 0:

            login_exist = call('select exists '
                     '(select * from person where login_per = %s)', [login], commit=False, fetchall=False)

            if login_exist[0] == 1:
                return jsonify({"error": "этот логин уже существует"}), 403

            elif login_exist[0] == 0:

                hash_pass = hash_password(password)

                call("insert into person (login_per, email_per, password_hash) "
                     "values (%s, %s, %s)", [login, email, hash_pass], commit=True, fetchall=False)

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


@app.route('/enter', methods=['POST'])
def enter():
    if request.method == 'POST':
        login = request.json['login']
        password = request.json['password']

        exist = call('select exists '
                     '(select * from person where login_per = %s)', [login], commit=False, fetchall=False)

        if exist[0] == 1:
            password_hash_form_bd = call('select password_hash from person '
                                         'where login_per = %s', [login], commit=False, fetchall=False)

            if check_password(password, password_hash_form_bd[0]):

                email = call("select email_per from person "
                             "where login_per = %s", [login], commit=False, fetchall=False)

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


if __name__ == '__main__':
    app.run(debug=True)
