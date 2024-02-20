from chartest import *
import json
import pyaudio
import sounddevice
from vosk import Model, KaldiRecognizer
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time
from characters import *

direction= 27
step = 26
EN_pin = 8

mymotortest = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin,GPIO.OUT)


GPIO.setup(direction, GPIO.OUT)
GPIO.setup(step, GPIO.OUT)

step_type = "Full"
steps = 200

step_delay = 0.0004
initial_delay = 0


def halt_step():
    GPIO.output(step, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(step, GPIO.LOW)

def left():
    GPIO.output(EN_pin,GPIO.LOW)
    mymotortest.motor_go(False,
                                step_type,
                                steps,
                                step_delay,
                                False,
                                initial_delay) 
    

def right():
    GPIO.output(EN_pin,GPIO.LOW)
    mymotortest.motor_go(True,
                                step_type,
                                steps,
                                step_delay,
                                False,
                                initial_delay)


GPIO.setup(20, GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

model = Model('/home/designerbtw/Desktop/vosk/small_model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

for i in range(4):
    GPIO.output(0, GPIO.HIGH)
    GPIO.output(1, GPIO.HIGH)
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(0, GPIO.LOW)
    GPIO.output(1, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    time.sleep(1)
    

def listen():
    data = stream.read(4000)
    if (rec.AcceptWaveform(data)) and (len(data) > 0):
        answer = json.loads(rec.Result())
        if answer['text']:
            yield answer['text']
while True:
    if GPIO.input(20) == False:
        for text in listen():
            x = list(text)
            for i in x:
                characters(i)

GPIO.cleanup()
