import os
import time
import pyttsx3
import random
import json
import geocoder
import requests
from pyfiglet import Figlet
import speech_recognition as rec
from dotenv import load_dotenv

load_dotenv()


triggers = ["hey will", "hi will", "hello will", "hey", "hi"]

responses = ["hey there", "hi What's up?", "hi there", "What's good?"]


def main():
    """
    Main function to run
    """
    start_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    print(f'Application StartTime: {start_time} \n {Figlet().renderText("Voice Control")}')
    print("Initiating microphone...\n")
    try:
        # for index, name in enumerate(rec.Microphone.list_microphone_names()):
            # print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
        initiate()
    except Exception as err:
        print(f"error : {err}")


def initiate():
    voice_input = getVoiceInput()
    if voice_input in triggers or "will" in voice_input:
        response = random.choice(responses)
        speak(
            f"{response}, Do you want to lock your PC, shutdown or check weather status?"
        )

        voice_input = getVoiceInput()
        if "weather" in voice_input:
            checkWeatherStatus()
        elif "lock" in voice_input:
            lockPC()
        elif "shutdown" in voice_input or "turn off" in voice_input:
            speak(f"Are you sure you want to turn off your computer?")
            shutDownPC()
    else:
        speak("Sorry, I do not understand your command, please repeat your command")
        initiate()


def getVoiceInput():
    """
        Function to get voice input using recognizer and microphone
    """
    recognizer = rec.Recognizer()

    with rec.Microphone() as mic:
        print("Listening...")
        #  minimum length of silence (in seconds) that will register as the end of a phrase
        recognizer.pause_threshold = 0.8
        # set the energy_threshold to a good value automatically.
        # listen for 1 second to calibrate the energy threshold for ambient noise levels
        recognizer.adjust_for_ambient_noise(mic)
        audio = recognizer.listen(mic)

        try:
            print("Recognising your voice")
            # default language is en-us
            recognized_audio = ""
            recognized_audio = recognizer.recognize_google(audio)

            print(f"User said : {recognized_audio}")
        except Exception as err:
            print(err)

    return recognized_audio


def speak(speech):
    """
        Function to speak to the user
    """
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(speech)
    engine.runAndWait()


def checkWeatherStatus():
    geo = geocoder.ip("me")
    API_KEY = os.getenv('API_KEY')
    exlude = "hourly,daily"  # weather data to exlude
    try:
        resp = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={geo.lat}&lon={geo.lng}&exclude={exlude}&appid={API_KEY}"
        )
        resp.raise_for_status()

        if resp.status_code == 200:
            data = json.loads(resp.content.decode("utf-8"))["current"]
            speak(
                f'Current Weather condition at {geo.city} is {data["weather"][0]["main"]} with a temperature of {data["temp"]} degree celsius.'
            )

        else:
            speak(f"Sorry I have connections issues at the moment")
    except Exception as err:
        print(err)
        speak(
            f"Sorry I have connections issues at the moment. Please check your internet connection"
        )


def lockPC():
    print("locking PC...")
    speak("Locking your PC, see ya!")
    os.system("Rundll32.exe user32.dll,LockWorkStation")


def shutDownPC():
    voice_input = getVoiceInput()
    if (
        "yeah" in voice_input
        or "yes" in voice_input
        or "shutdown" in voice_input
        or "turn off" in voice_input
    ):
        print("shutting down PC...")
        speak("Shutting Down your computer")
        os.system("shutdown /s /t 30")

    elif "no" in voice_input or "nope" in voice_input:
        speak(f"Okay bye then, see ya!")
    else:
        speak(f"Sorry, I do not understand,please repeat")
        shutDownPC()
