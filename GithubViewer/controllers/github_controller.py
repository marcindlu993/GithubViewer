import json
from GithubViewer import extension_fun
from collections import namedtuple
from flask import Flask, render_template, request
import person
from GithubViewer import app


@app.route('/')
def hello_world():
    return render_template('index.html', person =person)


@app.route('/', methods=['POST'])
def show_user():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    name = request.form['name']
    data = extension_fun.find_git_user(name)
    user = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    return render_template("userInfo.html", user=user)
