from datetime import datetime
from flask import Flask, render_template, url_for, redirect
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from forms import RegistrationForm, LoginForm

app = Flask(__name__,
            template_folder="templates/bootstrap/")

app.config['SECRET_KEY'] = '7134743777217A25432A462D4A614E64'
app.config["MONGO_URI"] = "mongodb://localhost:27017/hoqu"
mongo = PyMongo(app)
Bootstrap(app)


posts = [
    {
        'author': 'László Holler',
        'title': 'DEV Post 1',
        'content': 'First post of the day',
        'insert_date': '2019-09-10'
    },
    {
        'author': 'Gábor Gábor',
        'title': 'DEV Post 2',
        'content': 'Second post of the day',
        'insert_date': '2019-09-10'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login_2", methods=['GET', 'POST'])
def login_2():
    form = LoginForm()
    return render_template('login_2.html', title='Login', form=form)

@app.route("/base")
def base():
    return render_template('base.html', title='base')    


if __name__ == '__main__':
    app.run(debug=True)

