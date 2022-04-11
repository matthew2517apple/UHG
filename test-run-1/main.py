# main.py controller
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #return "Hello from Home page "
    return render_template('index.html')

@app.route('/about')
def about():
    #return 'Hello from about page'  
    return render_template('about.html') 

if __name__ == '__main__':
    app.run(debug=True)
