# main.py controller
from flask import Flask, redirect, request, url_for, render_template, jsonify
from db import get, create

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index.html')
def display():
    songs = get()
    return render_template('index.html', entries = songs)


@app.route('/add', methods=['POST'])
def add():
    create(request.form['title'], request.form['artist'], request.form['genre'])
    return redirect(url_for('display'))
    #create(request.get_json())
    #return "song added"

if __name__ == '__main__':
    app.run(debug=True)
