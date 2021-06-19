import speech_recognition as sr #convert speech to text
from Modules.Weather import get_weather
import requests, os
import pyttsx3 
from Modules.internet import SpeedTest
from datetime import datetime
from arrays import us_cities, us_states
import requests
import time
from GoogleNews import GoogleNews


input = sr.Recognizer()
engine = pyttsx3.init()
# googlenews = GoogleNews(lang='en', period='5d')

def talk(t):
    engine.say(t)
    engine.runAndWait()

def record():
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio) 
        except sr.UnknownValueError:
            return ""
        return data

def fetch_microphone_input(i):
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio) 
            data = data.lower()
            respond(data)
        except sr.UnknownValueError:
            return "Sorry I did not hear your question, Please repeat again."
        return data

def respond(text):
    data = str(text)
    data = data.lower()
    print(data)
    if 'weather' in data:
        for i in us_cities:
            if i.lower() in data:
                weather = get_weather(i)
                talk(f'Location: {str(weather[0])}')
                talk(f"Description: {str(weather[1])}")
                talk(f"Temprature: {str(weather[2])}")
                return
        for i in us_states:
            if i.lower() in data:
                weather = get_weather(i)
                talk(f'Location: {str(weather[0])}')
                talk(f"Description: {str(weather[1])}")
                talk(f"Temprature: {str(weather[2])}")
                return
        talk('Invalid US City or State')
    elif 'internet' in data:
        if 'speed' in data:
            sped = SpeedTest()
            talk('Connecting to server...')            
            sped.getBestServer()
            talk('Testing download and upload speed...')
            sped.download_upload()
    elif 'what time' in data or "the time" in data:
        talk(datetime.today().strftime("%I:%M %p"))
    elif 'google news' in data or 'news' in data:
        data_arr = data.split(' ')
        googlenews = GoogleNews(lang='en', period='7d')
        for i, e in enumerate(data_arr):
            if e == 'news':
                if data_arr[i - 1] != 'google': 
                    googlenews.search(str(data_arr[i - 1]))
                else:
                    googlenews.search(str(data_arr[i + 1]))
        googlenews.get_page(1)
        r = googlenews.page_at(1)
        talk(r[0]['title'])
        talk('Posted: ' + r[0]['date'])
        talk('Description: ' + r[0]['desc'])
    else:
        url = 'http://localhost:5000/'
        myobj = {'text': f'{data}'}

        x = requests.post(url, json = myobj)
        talk(x.text)
        
