import pyttsx3
import speech_recognition as sr
#for web searching
import webbrowser
import datetime
import pyjokes


def sptext():                             #listening
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        """Reading"""
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print(" Not Understand ")

#calling the function
#sptext()

def speechtx(x):
    engine = pyttsx3.init()
    #by default we have two voices in the system male and female u can used either by installing
    #We r going to set properties
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id) #for 0 we get male voice and 1 we get female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130) #Set the speed according to you after 130 the voice gets slow down
    engine.say(x)
    engine.runAndWait()
speechtx("hello welcome to Whoosh-Tech")

