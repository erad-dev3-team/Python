from datetime import datetime
from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from forms import RegistrationForm, LoginForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required

app = Flask(__name__,
            template_folder="templates/bootstrap/")

app.config['SECRET_KEY'] = '7134743777217A25432A462D4A614E64'
app.config["MONGO_URI"] = "mongodb://localhost:27017/hoqu"
mongo = PyMongo(app)
users = mongo.db.users
Bootstrap(app)


@app.route("/")
@app.route("/home")
def home():
    form = LoginForm()
    return render_template('home.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        query = request.args
        data = mongo.db.users.find_one(query)

        #data = request.get_json() 
    
   
    if request.method == 'POST':
            #Adding a Task  
        email=request.values.get("email")  
        password=request.values.get("password")  
        users.insert({ "email":email, "password":password})  
        return redirect("/home") 
        ''''email =  data['email']
        password =  data['password']
        if email is not None and password is not None:
            mongo.db.users.insert_one(data)
            return jsonify({'ok': True, 'message': 'User created successfully!'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400    '''
    form = LoginForm()
    return render_template('login.html', title='Login', form=form, data=data)

@app.route("/<ObjectId:task_id>")
def show_post(post_id):
    post = mongo.db.tasks.find_one_or_404(post_id)
    return render_template("posts.html", posts=post)

@app.route("/base")
def base():
    return render_template('base.html', title='base')

if __name__ == '__main__':
    app.run(debug=True)

