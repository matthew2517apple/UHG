# app.py controller
from flask import Flask, redirect, request, url_for, render_template, jsonify
from data import get_songs

app = Flask(__name__)

# home
@app.route('/')
def home():
    return render_template('home.html')

# about page
@app.route('/about')
def about():
    return render_template('about.html')

# display songs
@app.route('/display')
def display():
    songs = get_songs()
    return render_template('display.html', songs = songs)
    #return jsonify(songs)

#Single song
@app.route('/songs/<int:id>/')
def song(id):
    return render_template('song.html', id=id)

if __name__ == '__main__':
    app.run(debug=True)
