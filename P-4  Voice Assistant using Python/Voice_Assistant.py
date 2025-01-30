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
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for 1 second to handle ambient noise
        # audio = recognizer.listen(source,timeout=5)
        # """Reading"""
        # try:
        #     print("Recognizing...")
        #     data = recognizer.recognize_google(audio)
        #     print(f"Recognized: {data}")
        #     return data
        # except sr.UnknownValueError:
        #     print("Could not understand audio")
        #     return ""
        try:
            audio = recognizer.listen(source, timeout=10)  # Increased timeout to 10 seconds
        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
            return ""
        except Exception as e:
            print(f"An error occurred: {e}")
            return ""
        """Reading"""
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(f"Recognized: {data}")
            return data
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""

#calling the function
#sptext()

def speechtx(x):
    print(f"Speaking: {x}")  # Debug message
    engine = pyttsx3.init()
    #by default we have two voices in the system male and female u can used either by installing
    #We r going to set properties
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id) #for 0 we get male voice and 1 we get female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130) #Set the speed according to you after 130 the voice gets slow down
    engine.say(x)
    engine.runAndWait()

# Calling the function
# speechtx("hello welcome to Whoosh-Tech")
if __name__ == '__main__':
    print("Testing speech recognition...")
    # recognized_text = sptext()
    # if recognized_text.lower() == "hello":
        # pass
        # print("Triggering speech...")
        # speechtx("Hello Sir, How can I help you today?")
    data1 = sptext().lower()
    if "your name" in data1:
        name = "my name is jarvis"
        speechtx(name)
    elif "old are you" in data1:
        age = "i m 200 years old"
        speechtx(age)
    elif 'time now' in data1:
        time = datetime.datetime.now().strftime("%I%M%p")
        speechtx(time)
    elif 'play song' in data1:
        print("Opening YouTube...")  # Debug message
        webbrowser.open_new("https://www.youtube.com/watch?v=uxy254BGsxM&list=RDuxy254BGsxM&start_radio=1")
    elif 'google' in data1:
        webbrowser.open_new("https://www.google.com/")
    elif "joke" in data1:
        joke_1 = pyjokes.get_joke(language="en",category="neutral")
        print(joke_1)
        speechtx(joke_1)
    

    # else:
    #     print("Thanks")

