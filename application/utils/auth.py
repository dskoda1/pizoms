from functools import wraps
from flask import request, g, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature
from index import app

TWO_WEEKS = 1209600


def generate_token(user, expiration=TWO_WEEKS):
    s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    token = s.dumps({
        'id': user.id,
        'email': user.email,
    }).decode('utf-8')
    return token

def verify_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except (BadSignature, SignatureExpired):
        return None
    return data

def get_auth_header(req):
    json = req.get_json()
    if not json or 'headers' not in json:
        return req.headers.get('Authorization', None)

    json = json['headers']
    if not json or 'Authorization' not in json:
        return req.headers.get('Authorization', None)

    return json['Authorization']


# TODO: Create a decorator for admin functionality
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_auth_header(request)

        if token:
            string_token = token.encode('ascii', 'ignore')
            user = verify_token(string_token)
            if user:
                g.current_user = user
                return f(*args, **kwargs)

        return jsonify(message="Authentication is required to access this resource"), 401

    return decorated
