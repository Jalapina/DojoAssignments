from flask import Flask, render_template, redirect, request, session

app=Flask(__name__)
app.secret_key='this is a secret_key'

@app.route('/')
def home():
    return render_template('home.html')

app.run(debug=True)

