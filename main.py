import subprocess
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
import os
from AppOpener import open, close

jarvis = pyttsx3.init('sapi5')
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice', voices[0].id)


def speak(audio):
    jarvis.say(audio)
    jarvis.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis.How can I help you sir....")


def take_command():
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
        speak("Say that again please sir......")
        return "None"
    return query


def run_alexa():
    wishMe()
    while True:
        command = take_command().lower()

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('Current time is ' + time)

        elif 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'tell me about' in command:
            speak('Searching Wikipedia...')
            look_for = command.replace('tell me about', '')
            info = wikipedia.summary(look_for, 1)
            print(info)
            speak(info)

        elif 'joke' in command:
            speak('searching jokes...')
            speak(pyjokes.get_joke())

        elif 'date' in command:
            speak('Sorry Sir, I am a assistant. I cant go with you')

        elif 'spotify' in command:
            open("spotify")

        elif 'chrome' in command:
            open("google_chrome")

        elif 'visual studio code' in command:
            open("Visual Studio Code")

        elif 'word' in command:
            open("Word")

        elif 'excel' in command:
            open("Excel")

        elif 'powerpoint' in command:
            open("PowerPoint")

        elif 'illustrator' in command:
            subprocess.Popen(
                "C:\Program Files\Adobe\Adobe Illustrator 2023\Support Files\Contents\Windows\Illustrator.exe")
            os.startfile(subprocess.Popen)

        elif 'open youtube' in command:
            speak('Open YouTube...')
            pywhatkit.search("https://www.youtube.com")

        elif 'open facebook' in command:
            speak('Open Facebook...')
            pywhatkit.search("https://www.facebook.com")

        elif 'play music' in command:
            music_dir = 'D:\Media\Torrent\All movie file\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'option' in command:
            option()

        elif 'stop' in command:
            exit(jarvis)


def option():
    print()
    print("1. Open <any_name> TO OPEN APPLICATIONS")
    print("2. Close <any_name> TO CLOSE APPLICATIONS")
    print()
    open("help")
    print("TRY 'OPEN <any_key>'")
    while True:
        inp = input("ENTER APPLICATION TO OPEN / CLOSE: ").lower()
        if "close " in inp:
            app_name = inp.replace("close ", "").strip()
            close(app_name)
        if "open " in inp:
            app_name = inp.replace("open ", "")
            open(app_name)
        if "exit " in inp:
            jarvis = inp.replace("exit", "")
            exit(jarvis)


while True:
    run_alexa()
