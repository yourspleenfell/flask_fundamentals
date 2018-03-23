from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/ninja')
def ninja():
    ninjacolor = 'none'
    return render_template('/ninja.html', ninjacolor = ninjacolor)

@app.route('/ninja/<ninjacolor>')
def blue(ninjacolor):
    return render_template('/ninja.html', ninjacolor = ninjacolor)

app.run(debug=True)