import os
import jwt
import random
import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import *
from private import private

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/voter"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/user', methods=['POST'])
def create_user():

    data = request.get_json()

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message' : 'Email already registered!'})

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(name=data['name'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message' : 'Success!'})

@app.route('/poll', methods=['POST'])
@private
def create_poll(current_user):

    data = request.get_json()
    key = random.randint(100000, 999999)

    if Poll.query.filter_by(key=key).first():
        return jsonify({'message' : 'Please, try again!'})
    
    new_poll = Poll(name=data['name'], key=key, user_id=current_user.id, secret=data['secret'])
    db.session.add(new_poll)
    db.session.commit()

    for option in data['options']:
        new_option = Option(name=option, poll_id=new_poll.id)
        db.session.add(new_option)
    
    db.session.commit()

    return jsonify({'message' : 'Success!', "key" : key})

@app.route('/user/polls/', methods=['GET'])
@private
def get_all_polls(current_user):
    polls = Poll.query.filter_by(user_id=current_user.id).all()
    output = []
    for poll in polls:
        poll_data = {}
        poll_data["id"] = poll.id
        poll_data["key"] = poll.key
        poll_data["name"] = poll.name
        poll_data["secret"] = poll.secret
        poll_data["options"] = []
        for option in poll.options:
            option_data = {}
            option_data["name"] = option.name
            option_data["id"] = option.id
            option_data["votes"] = len(option.votes)
            if not poll.secret:
                option_data["names"] = []
                for vote in option.votes:
                    user_id = vote.user_id
                    user = User.query.get(user_id)
                    option_data["names"].append(user.name)
            poll_data["options"].append(option_data)
        output.append(poll_data)
    return jsonify(output)

@app.route('/poll/<int:key>', methods=['GET'])
@private
def get_one_poll(current_user, key):

    poll = Poll.query.filter_by(key=key).first()
    if poll:
        output = {}
        output["id"] = poll.id
        output["name"] = poll.name
        output["secret"] = poll.secret
        output["options"] = []
        for option in poll.options:
            output_option = {}
            output_option["name"] = option.name
            output_option["id"] = option.id
            output["options"].append(output_option)

        return jsonify(output)
        
    return jsonify({'message' : 'Not found!'})


@app.route('/poll', methods=['DELETE'])
@private
def delete_poll(current_user):
    id = request.json['id']
    me = Poll.query.get(id)

    if not me:
        return jsonify({'message' : 'Not found!'})

    if current_user.id != me.user_id:
        return jsonify({'message' : 'Not allowed!'})
    
    db.session.delete(me)
    db.session.commit()

    return jsonify({'message' : 'Successfully deleted!'})


@app.route('/vote', methods=['POST'])
@private
def create_vote(current_user):

    data = request.get_json()
    poll_id = Option.query.get(data['option_id']).poll_id

    if Vote.query.filter_by(poll_id=poll_id, user_id=current_user.id).first():
        return jsonify({'message' : 'You have already voted!'})

    new_vote = Vote(user_id=current_user.id, option_id=data['option_id'], poll_id=poll_id)
    db.session.add(new_vote)
    
    db.session.commit()    

    return jsonify({'message' : 'Success!'})


@app.route('/login', methods=['POST'])
def login():
    auth=request.authorization
    email = auth.username
    password = auth.password

    if not auth or not email or not password:
        return jsonify({'message' : 'Invalid email or password!'})

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message' : 'Invalid email or password!'})
    
    if not check_password_hash(user.password, password):
        return jsonify({'message' : 'Invalid email or password!'})

    token = jwt.encode({'id' : str(user.id), 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

    return jsonify({'token' : token})


if __name__ == '__main__':
  app.run(debug=True)
