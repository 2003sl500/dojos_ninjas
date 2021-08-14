from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojos import Dojos
from flask_app.models.ninjas import Ninjas

@app.route('/')
def base_route():
    return redirect('/index/dojos')

@app.route('/index/dojos')
def index_dojos():
    dojo_info = Dojos.get_all()
    return render_template('dojo.html', dojo_info = dojo_info)

@app.route('/index/ninjas')
def index_ninjas():
    ninja_info = Ninjas.get_all()
    return render_template('show_ninjas.html', ninja_info = ninja_info)

@app.route('/create/dojos', methods = ['POST'])
def create_dojos():
    data = {
        "name": request.form['name']
    }
    Dojos.create(data)
    return redirect('/index/dojos')

@app.route('/create/ninja_page')
def create_ninja_page():
    dojo_names = Dojos.get_all()
    return render_template('ninja.html', dojo_names = dojo_names)

@app.route('/create/ninjas', methods = ['POST'])
def create_ninjas():
    data = {
        "dojo_id": request.form['dojo_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age']
    }
    Ninjas.create(data)
    return redirect('/index/ninjas')

@app.route('/index/dojo/ninjas/<int:id>/<name>')
def dojos_ninjas(id, name):
    ninja_info = Ninjas.show_dojo_ninjas(id)
    session['name'] = name
    return render_template('dojos_ninjas.html', ninja_info = ninja_info)