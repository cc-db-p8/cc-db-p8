# coding=utf-8
from flask import Flask, url_for, render_template
import models
app = Flask(__name__)

@app.route('/')
def hello_world():
    user = models.User.get_user('toot')
    posts = models.Post.get_posts(user['username'])

    return render_template('index.html', user=user, posts=posts)