import RPi.GPIO as GPIO
import time
from flask import Flask
app = Flask(__name__)

@app.before_first_request
def startup():
    servoPIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

@app.route('/cozmoguardOpen')
def cozmoguardOpen():
    
    p = GPIO.PWM(17, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    
    p.ChangeDutyCycle(10)
    time.sleep(5.0)
    p.ChangeDutyCycle(4)
    time.sleep(0.5)
    
    p.stop()
    return 'Open The Door'


@app.route('/cozmoguardClose')
def cozmoguardClose():
    return 'Close The Door'



