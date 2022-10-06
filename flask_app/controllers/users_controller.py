from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.users_model import User

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def index():
    all_users = User.get_all()
    return render_template ('index.html', users=all_users)

@app.route('/new')
def new_user():
    return render_template('new_user.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    User.create_user(request.form)
    return redirect ('/users')

@app.route('/show/<int:id>')
def show_user(id):
    data={
        "id":id
    }
    return render_template('show.html',user=User.get_one(data))

@app.route('/edit/<int:id>')
def edit_user(id):
    data={
        "id":id
    }
    return render_template ("edit.html",user=User.get_one(data))

@app.route('/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect ('/users')

@app.route('/delete/<int:id>')
def destroy(id):
    data={
        "id":id
    }
    User.delete(data)
    return redirect ('/users')