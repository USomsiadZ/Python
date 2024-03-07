from xml.dom.minidom import Element
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
print('Asystent głosowy andrzej')
speak('jestem asystentem głosowym andrzej czym moge ci służyć')
def getText():
    try:
        
        with sr.Microphone() as source:
            
            audio = r.listen(source)
            print(type(audio))
            text = r.recognize_google(audio, language='pl-PL')
            print('Nasłuchuje')
            if text == "":
                print('1')
                return None
            else:
                print('2')
                return text
    except:
        print('niema nic')
        return None
def czy_zawiera(string,slowa):
    return [element for element in slowa if element in string.lower()]
print("aby wyjsc powiedz 'Dowidzenia")
wykryj = ['andrzej','bocie','dzarwis']
wyjdz = ['dowidzenia','papa']
szukaj= ['szukaj']
#print(""*50,end='\r')
while True:
    time.sleep(1)
    cur = getText()
    #print(cur)
    
    if cur != None:
        if len(czy_zawiera(cur,wykryj)):
            print('zawiera')
            if len(czy_zawiera(cur,wyjdz)):
                speak('papa')
                break
            elif len(czy_zawiera(cur,szukaj)):
                print('nie zawiera')
                link = cur.lower().split('' + czy_zawiera(cur,szukaj)[0] + '')[1]
                speak('oto co udało mi się znaleść')
                url= 'https://www.google.com/search?q=' + link.replace(" ","+").replace("?", '%3f')
                webbrowser.open(url)
    else:
        print("none")

