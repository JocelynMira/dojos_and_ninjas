from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo_model, ninja_model



# index page 
@app.route('/ninjas')
def ninja_index():
    return render_template('ninja.html', dojos = dojo_model.Dojo.get_dojos())


# CREATE
@app.route('/new_ninja', methods=['POST'])
def new_ninja():
    data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "age": request.form['age'],
            "dojo_id": request.form['dojo_id']
    }
    ninja_model.Ninja.save(data)
    return redirect ('/')

# READ
@app.route('/all_ninjas')
def get_ninjas():
    ninjas = ninja_model.Ninja.get_ninjas()
    return render_template ('index.html', ninjas = ninjas)

@app.route('/one_ninja/<int:id>')
def get_one_ninja(id):
    dojo = dojo.get_one_ninja(id)
    return render_template ('index.html', dojo)