# -*- coding: utf-8 -*-
from alayatodo import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    todos = db.relationship('Todos', backref='users', lazy=True)
    
    def set_pass(self, password):
        self.password = generate_password_hash(password)
        
    def check_pass(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return {'id': self.id, 'username': self.username}

class Todos (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return {'id': self.id, 'user_id': self.user_id, 'description': self.description, 'status': self.status}