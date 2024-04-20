# main.py controller
from flask import Flask, redirect, request, url_for, render_template, jsonify
from db import get_branches, get_customers, get_one_branch, create, get_perryridge_customers

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")    

@app.route('/display')
def display():
    #branches = get_branches()
    #return render_template('display.html', branches = branches)
    menu_items = get_menu()
    return render_template('display.html', menu_items = menu_items)        # <-- EDIT HERE.

#Single branch
#@app.route('/branches/<int:id>/')
#def branch(name):
#    branch = get_one_branch(name)
#    return render_template('branch.html', branch=branch)

@app.route('/insert_form')
def insert_form():
    return render_template('insert.html')

@app.route('/perryridge')
def perryridge():                                                                # <-- EDIT HERE.
    customers = get_perryridge_customers()                                        # <-- EDIT HERE.
    return render_template('display.html', customers = customers)

@app.route('/add', methods=['POST'])
def add():
    create(request.form['customer_name'], request.form['customer_street'], request.form['customer_city'])   # <-- EDIT HERE.
    return redirect(url_for('display'))

if __name__ == '__main__':
    app.run(debug=True)
