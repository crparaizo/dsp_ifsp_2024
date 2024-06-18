import speech_recognition as sr
import pyfirmata
from pyfirmata import Arduino
from time import sleep
import pyttsx3

port = "COM"
board = Arduino(port)
bluePin = 10
redPin = 11
engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone()

while True:

    with mic as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(command)

    except sr.UnknownValueError:
        command = "algum erro"
        engine.say(command)
        engine.runAndWait()
        print("Error")
    command = command.lower()

    if "blue" in command:
        # command.replace("turn","")
        board.digital[bluePin].write(1)
        sleep(3)
        board.digital[bluePin].write(0)
        engine.say("blue led is blinking")
        engine.runAndWait()

    if "red" in command:
        # command.replace("turn","")
        board.digital[bluePin].write(1)
        sleep(3)
        board.digital[bluePin].write(0)
        engine.say("blue led is blinking")
        engine.runAndWait()
