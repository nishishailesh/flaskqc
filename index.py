#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloo():
    return 'Hello, try World!'+__name__
