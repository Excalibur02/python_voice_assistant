import datetime
import requests
import pywhatkit
import pyttsx3
import webbrowser
import speech_recognition as sr
import os


listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 120)


def greet():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        engine.say("Good Morning !")
        engine.say(" this is kashish 1 poin o at your service ")
        engine.say("what can i do for you ")
        engine.runAndWait()
    elif 12 <= hour < 16:
        engine.say("Good afternoon ! ")
        engine.say(" this is kashish 1 poin o at your service ")
        engine.say("what can i do for you ")
        engine.runAndWait()
    else:
        engine.say("Good evening  !")
        engine.say(" this is kashish 1 poin o at your service ")
        engine.say("what can i do for you ")
        engine.runAndWait()


greet()


def talk(text):
    engine.say(text)
    engine.runAndWait()
    print(text)


def kashish_cmd():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            # sr.adjust_for_ambient_noise(source, duration=0.2)
            listener.pause_threshold = 2
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)

            cmd = cmd.lower()
            if "kashish" in cmd:
                cmd = cmd.replace("kashish", "")

    except Exception as e:
        talk("Sorry I could not understand what you said, can you please repeat yourself")

    return cmd


def run_kashish():
    cmd = kashish_cmd()
    # print(cmd)
    if "play" in cmd:
        song = cmd.replace("play", "")
        talk("wait a bit i am playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in cmd:
        time = datetime.datetime.now().strftime("%H hours and %M minutes")
        talk("Current time is " + time)
    elif "weather" in cmd:
        city = "new delhi"
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=29b56202195e471e213de207a4bb112f"
        json_data = requests.get(api).json()
        conditions = json_data['weather'][0]['main']
        temp = round((json_data['main']['temp'] - 273.15000), 5)
        talk(conditions + "would best describe the current weather condition in Delhi ")
        talk(f"the temperature feels somewhat around {temp} degree Celcius as of now")
    elif "google" in cmd:
        data = cmd.replace("google", "")
        data = data.replace("search", "")
        talk("Here is your google search ")
        webbrowser.open("www.google.co.in/search?q="+data)
    elif "shut down "  in cmd:
        break




#
# with open('speech.txt', mode='w') as file:
#     file.write(kashish_cmd())


run_kashish()
