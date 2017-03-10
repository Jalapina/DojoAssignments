from flask import Flask, render_template, redirect, request,session

app =  Flask(__name__)
app.secret_key='this is the secret_key'

@app.route('/')
def index():
    import random
    x = random.randrange(0, 101)
    session['num']=x #assigning a random number to ver 'num'
    print session['num']
    return render_template('index.html')    #Returning an html page

@app.route('/answer', methods=['POST'])     
def ans():
    number = session['num']
    submit=request.form['guess'] #Assigning the input to ver submit 
    submit=int(submit)
    
    if  submit==number:
        message='YEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSsssssssss!'
        print 'this is correct'
        return render_template('index.html', message=message)
    elif submit>number:
        print 'Too big'
        message='NO! that is too big! Try again'
        return render_template('index.html', message=message) 
    elif submit<number:
        print 'too small'
        message='Too low! Try again'
        return render_template('index.html', message=message)
    return render_template('index.html')  
@app.route('/replay')
def restart():
    session.pop('num')
    return redirect('/')
app.run(debug=True) 
