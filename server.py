from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def services():
    return render_template('services.html')
@app.route('/donate')
def donate():
    return render_template('donate.html')
