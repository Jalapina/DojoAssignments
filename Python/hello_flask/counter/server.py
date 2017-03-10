from flask import Flask, render_template, request, redirect,session

app=Flask(__name__)
app.secret_key='this is the secret_key'

@app.route('/')
def home():
    if 'counter' not in session:
        session['counter']=0
    else:
        session['counter']+=1
    
    return render_template('home.html')

@app.route('/add', methods=['POST'])
def adding():
    session['counter']+=1
    # session.close()
    return redirect('/')

@app.route('/restore', methods=['POST'])
def restart():
    # session['counter']
    session.clear()
    return redirect('/')





app.run(debug=True)
