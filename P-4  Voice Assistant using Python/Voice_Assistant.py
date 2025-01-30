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
sptext()
