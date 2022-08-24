import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

from wikipedia import exceptions


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir!')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon Sir!')
    else:
        speak('Good Evening Sir!')

    speak('I am jarvis assistant, how can i help you?')


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    pass



if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Browsing
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")

        elif 'open stack overflow'  in query:
            speak("Opening stack overflow")
            webbrowser.open("https://stackoverflow.com/")

        elif 'open stackoverflow'  in query:
            speak("Opening stack overflow")
            webbrowser.open("https://stackoverflow.com/")

        elif 'open 10 fast fingers' in query:
            speak("Opening 10 fast fingers")
            webbrowser.open("https://10fastfingers.com/")

        elif 'open 10fastfingers' in query:
            speak("Opening 10 fast fingers")
            webbrowser.open("https://10fastfingers.com/")


        # Time and Date
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:   
            strDate = datetime.date.today()
            speak(f"Sir, the date is {strDate}")


        # Opening applications
        elif 'open code' in query:
            speak("Opening visual studio code")
            codePath = "C:\\Users\\91904\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open cmd' in query:
            speak("Opening command prompt")
            cmdPath = "C:\\Users\\91904\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt"
            os.startfile(cmdPath)

        elif 'open command prompt' in query:
            speak("Opening command prompt")
            cmdPath = "C:\\Users\\91904\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt"
            os.startfile(cmdPath)


        # Personal queries
        elif 'how are you' in query:
            speak("I am doing fine, thanks for asking!")

        elif 'where do you live' in query:
            speak("I live in harjot's computer")

        elif 'where are you' in query:
            speak("I am in harjot's computer")

        elif 'stop' in query:
            speak("quitting sir, see you again!")
            exit()

        elif 'quit' in query:
            speak("quitting sir, see you again!")
            exit()
        
        elif 'who are you' in query:
            speak("I am jarvis assistant, and i am there to help you!")

        elif 'who created you' in query:
            speak("I am created by Harjot Singh and i am always there to help you")


       


        