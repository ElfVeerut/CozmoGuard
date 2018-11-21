#FLASK_APP=cozmo_servo.py flask run
#import RPi.GPIO as GPIO

import time
from flask import Flask, redirect, url_for, escape, request
app = Flask(__name__)
app.secret_key = 'KwLWtuXWSX'
password = '123456'
session = {}
#@app.before_first_request
#def startup():
#    servoPIN = 17
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(servoPIN, GPIO.OUT)

# True == Logged in
# False == Not logged in
@app.route('/')
def index():
    print(session)
    if 'password' in session:
        if password == session['password']:
            return 'True'
    return 'False'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form.get('password'))
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('password', None)
    return redirect(url_for('index'))

@app.route('/cozmoguardOpen')
def cozmoguardOpen():
    if 'password' in session:
        if password == session['password']:
            #    p = GPIO.PWM(17, 50) # GPIO 17 for PWM with 50Hz
            #    p.start(2.5) # Initialization
            #
            #    p.ChangeDutyCycle(10)
            #    time.sleep(5.0)
            #    p.ChangeDutyCycle(4)
            #    time.sleep(0.5)
            #
            #    p.stop()
            # Open the door
            return 'True'
    else:
        return 'False'

@app.route('/cozmoguardClose')
def cozmoguardClose():
    if 'password' in session:
        if password == session['password']:
            # Close the door
            return 'True'
    else:
        return 'False'