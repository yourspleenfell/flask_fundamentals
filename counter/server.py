from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'NotMySecret'

@app.route('/')
def count():
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
        session['count'] = 1
    return render_template('index.html')

@app.route('/plus2', methods=['POST'])
def plus2():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)