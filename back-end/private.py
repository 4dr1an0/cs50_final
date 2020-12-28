import jwt
import os
from functools import wraps
from flask import Flask, request, jsonify
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

def private(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message' : 'Authentication required!'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            current_user = User.query.get(data["id"])
        except:
            return jsonify({'message' : 'Invalid token!'})
        
        return f(current_user, *args, **kwargs)
    
    return decorated