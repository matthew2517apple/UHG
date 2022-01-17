# main.py controller
from flask import Flask, redirect, request, url_for, render_template, jsonify
from db import get, create

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/insert.html')
def display():
    songs = get()
    return render_template('insert.html', entries = songs)


@app.route('/add', methods=['POST'])
def add():
    create(request.form['title'], request.form['artist'], request.form['genre'])
    return redirect(url_for('display'))

if __name__ == '__main__':
    app.run(debug=True)
