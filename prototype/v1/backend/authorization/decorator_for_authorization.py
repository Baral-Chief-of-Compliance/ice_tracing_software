import jwt
from functools import wraps
from app import request, jsonify, app
from app.use_db.tools import quarry


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

            email_exist = quarry.call('select exists '
                               '(select * from person where email_per = %s)', [email], commit=False, fetchall=False)

            if email_exist[0] == 0:
                raise RuntimeError('User not found')

            login = quarry.call('select login_per from person where email_per = %s', [email], commit=False, fetchall=False)
            return f(login[0], *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify
