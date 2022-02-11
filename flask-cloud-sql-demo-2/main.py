# main.py controller
from flask import Flask, redirect, request, url_for, render_template, jsonify
from db import get_songs, get_one_song, create

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")    

@app.route('/display')
def display():
    songs = get_songs()
    return render_template('display.html', songs = songs)

#Single song
@app.route('/songs/<int:id>/')
def song(id):
    song = get_one_song(id)
    return render_template('song.html', song=song)

@app.route('/insert_form')
def insert_form():
    #songs = get_songs()
    #return render_template('insert.html', songs = songs)
    return render_template('insert.html')


@app.route('/add', methods=['POST'])
def add():
    create(request.form['title'], request.form['artist'], request.form['genre'])
    return redirect(url_for('display'))

if __name__ == '__main__':
    app.run(debug=True)
