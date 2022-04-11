# main.py controller
from flask import Flask, render_template
from db import get_songs

app = Flask(__name__)

@app.route('/')
def home():
    #return "Hello from Home page "
    return render_template('index.html')

@app.route('/about')
def about():
    #return 'Hello from about page'  
    return render_template('about.html') 

@app.route('/display')
def display():
    songs_ = get_songs()
    return render_template('display.html', songs = songs_) 

if __name__ == '__main__':
    app.run(debug=True)
