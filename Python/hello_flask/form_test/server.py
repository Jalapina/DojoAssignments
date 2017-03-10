from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def index():
    print 'It is working'
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    print 'Still working'
    user_email=request.form['useremail']
    user_location=request.form['location']
    user_lan=request.form['lan']
    user_comment=request.form['comment']
    return render_template('returning.html', email=user_email, loc=user_location, lan=user_lan, comment=user_comment)

app.run(debug=True)
