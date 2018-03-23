from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThePathThroughTheWoodsIsRough'

import random

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['num'] = random.randint(1,100)
    print session['num']
    session['guess'] = int(request.form['guess'])
    if (session['num'] > session['guess']):
        session['outcome'] = "You guessed too low!"
        session.pop('guess')
    elif (session['num'] < session['guess']):
        session['outcome'] = "You guessed too high!"
        session.pop('guess')
    elif (session['num'] == session['num']):
        session['outcome'] = "was the number :)"
        session.pop('guess')
    print request.form
    return redirect('/')

@app.route('/again')
def play_again():
    session.pop('num')
    session['outcome'] = 'none'
    return redirect('/')

app.run(debug=True)