#!/usr/bin/env python3

import logging  
import socket 
import udp_connect as udp 
from flask import request, redirect, url_for, render_template, send_from_directory
from flask import Flask

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

#app = Flask(__name__, static_url_path='/static', static_folder='/static')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        msg = request.form['fname']
        logging.info(msg)
        client = udp.init_client()
        udp.send_msg(msg, client)
        udp.close_client(client)
        return redirect("index.html")
    else:
        return render_template("index.html")


