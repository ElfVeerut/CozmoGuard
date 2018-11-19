#FLASK_APP=cozmo_servo.py flask run
#import RPi.GPIO as GPIO
import time
from flask import Flask
app = Flask(__name__)

#@app.before_first_request
#def startup():
#    servoPIN = 17
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(servoPIN, GPIO.OUT)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
            return 'Logged in as ' + username + '<br>' + \
                "<b><a href = '/logout'>click here to log out</a></b>"
                    return "You are not logged in <br><a href = '/login'></b>" + \
                        "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
            return '''
                
                <form action = "" method = "post">
                <p><input type = text name = username/></p>
                <p<<input type = submit value = Login/></p>
                </form>
                
                '''

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/cozmoguardOpen')
def cozmoguardOpen():
    
#    p = GPIO.PWM(17, 50) # GPIO 17 for PWM with 50Hz
#    p.start(2.5) # Initialization
#
#    p.ChangeDutyCycle(10)
#    time.sleep(5.0)
#    p.ChangeDutyCycle(4)
#    time.sleep(0.5)
#
#    p.stop()
    return 'Open The Door'


@app.route('/cozmoguardClose')
def cozmoguardClose():
    return 'Close The Door'

