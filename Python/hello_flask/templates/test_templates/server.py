from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/ninjas')
def index():
    return render_template("index.html")


@app.route('/')
def greetings():
    retutn render_template('greeting.html')

app.run(debug=True)

