from flask import Flask
app = Flask(__name__)

@app.route('/cozmoguardOpen')
def cozmoguardOpen():
    return 'Open The Door'

@app.route('/cozmoguardClose')
def cozmoguardClose():
    return 'Close The Door'



