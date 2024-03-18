
import speech_recognition as sr
import pyttsx3 as tts
import time
import webbrowser


r = sr.Recognizer()
engine = tts.init()
engine.setProperty('voice',engine.getProperty('voices')[0].id)

chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def getText():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='pl-PL')
            return text
        except:
            return None

def contains(string, words):
    return [word for word in words if word in string.lower()]

while True:
    time.sleep(1)
    cur = getText()

    if cur:
        if contains(cur, ['andrzej','bocie','dzarwis']):
            if contains(cur, ['dowidzenia','papa']):
                speak('papa')
                break
            elif contains(cur, ['szukaj']):
                link = cur.lower().split('szukaj')[1]
                speak('oto co udało mi się znaleść')
                url = 'https://www.google.com/search?q=' + link.replace(" ","+").replace("?", '%3f')
                webbrowser.open(url)
