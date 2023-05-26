from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from flask_mysqldb import MySQL
import MySQLdb.cursors
from hash import check_password
import bcrypt


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
                print("пользователь вошел")
                return "user is enter"

            else:
                print("неправильный пароль")
                return "wrong password"

        else:
            print("такого логина нет")
            return "wrong login"




if __name__ == '__main__':
    app.run(debug=True)
