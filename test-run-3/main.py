# main.py controller
from flask import Flask, redirect, request, url_for, render_template, jsonify
from db import get_branches, get_customers, get_one_branch, create

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
    customers = get_customers()
    return render_template('display.html', customers = customers)

#Single branch
@app.route('/branches/<int:id>/')
def branch(name):
    branch = get_one_branch(name)
    return render_template('branch.html', branch=branch)

@app.route('/insert_form')
def insert_form():
    return render_template('insert.html')


@app.route('/add', methods=['POST'])
def add():
    create(request.form['customer_name'], request.form['customer_street'], request.form['customer_city'])
    return redirect(url_for('display'))

if __name__ == '__main__':
    app.run(debug=True)
