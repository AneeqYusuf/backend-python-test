# -*- coding: utf-8 -*-
class Config(object):
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/alayatodo.db'
    DATABASE = '/tmp/alayatodo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = 'development key'
    USERNAME = 'admin'
    PASSWORD = 'default'
    POSTS_PER_PAGE = 3
    WTF_CSRF_SECRET_KEY = 'extra secure layer'
    JWT_SECRET_KEY = 'another layer'
