from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo


# route to dojo main page
@app.route('/')
def dojo_index():
    return redirect('/all_dojos')

# CREATE
@app.route('/new_dojo', methods=['POST'])
def new_dojo():
    print(request.form)
    data = {
        'name' : request.form['name']
    }
    Dojo.save(data)
    return redirect ('/')

# READ 
@app.route('/all_dojos')
def get_dojos():
    dojos = Dojo.get_dojos() 
    return render_template ('index.html', all_dojos = dojos)

@app.route('/one_dojo/<int:id>')
def get_one_dojo(id):
    data = {
        'id': id
    }
    return render_template ('dojo_show.html', dojo = Dojo.get_dojo_with_ninjas(data) )