import os
import pyttsx3
import speech_recognition as rec
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("user") if os.getenv("user") else "hopeswiller"

def main():
    "Main function to run"
    print("Started ...")
    try:
        
        # voice_input = getVoiceInput()
        # if "lock" in voice_input:
        #     print('locking PC...')
        #     speak('Locking your computer')
        #     os.system("Rundll32.exe user32.dll,LockWorkStation")

        # elif "shutdown" in voice_input or "turn off" in voice_input:
        #     print('shutting down PC...')
        #     speak('Shutting Down your computer')
        #     os.system("shutdown /s /t 30")

        speak(f"Do you want to lock your computer, {user}?")
        controller()
    except Exception as err:
        print(f'error : {err}')



def controller():
    voice_input = getVoiceInput()

    if "yes" in voice_input:
        print('locking PC...')
        speak('Locking your computer')
        os.system("Rundll32.exe user32.dll,LockWorkStation")

    elif "no" in voice_input:
        speak('Okay Bye then....')

    else:
        speak('I do not understand your command, please repeat your command')
        controller()




def getVoiceInput():
    """
        Function to get voice input using recognizer and microphone
    """
    recognizer = rec.Recognizer()

    with rec.Microphone() as mic:
        print('Listening...')
        #  threshold seconds of no voice input to complete command
        recognizer.pause_threshold = 0.5
        audio = recognizer.listen(mic)

        # voice command identified
        try:
            print('Recognising your voice')
            # default language is en-us
            recognized_audio = ""
            recognized_audio = recognizer.recognize_google(audio)

            print(f'User said : {recognized_audio}')
        except Exception as err:
            print(err) 

    return recognized_audio


def speak(speech):
    """
        Function to speak to the user
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(speech)
    engine.runAndWait()
