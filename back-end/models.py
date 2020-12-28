from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

import uuid

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/voter"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

class Poll(db.Model):
    __tablename__ = "polls"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    key = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    options = db.relationship('Option', backref="polls", cascade="all, delete", passive_deletes=True, lazy=False)
    secret = db.Column(db.Boolean)

class Option(db.Model):
    __tablename__ = "options"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = db.Column(db.String, nullable=False)
    poll_id = db.Column(UUID(as_uuid=True), db.ForeignKey("polls.id", ondelete='CASCADE'), nullable=False)
    votes = db.relationship('Vote', backref="options", cascade="all, delete", passive_deletes=True, lazy=False)

class Vote(db.Model):
    __tablename__ = "votes"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    option_id = db.Column(UUID(as_uuid=True), db.ForeignKey("options.id", ondelete='CASCADE'), nullable=False)
    poll_id = db.Column(UUID(as_uuid=True), db.ForeignKey("polls.id", ondelete='CASCADE'), nullable=False)


