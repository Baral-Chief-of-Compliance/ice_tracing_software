from app.use_db.tools import quarry


def check_email_exist(email):
    email_exist = quarry.call('select exists '
                       '(select * from person where email_per = %s)', [email], commit=False, fetchall=False)

    return email_exist


def check_login_exist(login):
    login_exist = quarry.call('select exists '
                     '(select * from person where login_per = %s)', [login], commit=False, fetchall=False)

    return login_exist


def add_account_to_bd(login, email, hash_pass):
    quarry.call("insert into person (login_per, email_per, password_hash) "
         "values (%s, %s, %s)", [login, email, hash_pass], commit=True, fetchall=False)


def get_password_hash_from_bd(login):
    password_hash_form_bd = quarry.call('select password_hash from person '
                                 'where login_per = %s', [login], commit=False, fetchall=False)

    return password_hash_form_bd


def get_email(login):
    email = quarry.call("select email_per from person "
                             "where login_per = %s", [login], commit=False, fetchall=False)

    return email
