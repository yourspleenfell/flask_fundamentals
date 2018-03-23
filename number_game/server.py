from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThePathThroughTheWoodsIsRough'

import random

@app.route('/')
def index():
    session['num'] = random.randint(1,100)
    print session['num']
    return render_template('/index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if (session['num'] > guess):
        session['outcome'] = "You guessed too low! " + str(guess)
    elif (session['num'] < guess):
        session['outcome'] = "You guessed too high! " +  str(guess)
    elif (session['num'] == session['num']):
        session['outcome'] = "You gussed the number! The number was " + str(guess) + " :)"
    print request.form
    return redirect('/')

app.run(debug=True)