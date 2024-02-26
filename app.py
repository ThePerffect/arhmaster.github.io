from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('page_home.html')

@app.route("/about")
def about():
    return render_template('page_about.html')
    
@app.route("/contacts")
def contacts():
    return render_template('page_contacts.html')

