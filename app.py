# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import count_length


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods=["GET", "POST"])
def result():
    print(request.form["nickname"])
    user_nickname = request.form["nickname"]
    user_nickname_length = count_length(user_nickname)
    return render_template("results.html", user_nickname=user_nickname, user_nickname_length=user_nickname_length)