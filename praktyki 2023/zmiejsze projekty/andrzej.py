import pyttsx3
import speech_recognition as sr

# Inicjalizacja silnika syntezy mowy
engine = pyttsx3.init()
voice = engine.getProperty('voices')


polish_voice_index = None
for i, voice in enumerate(voice):
    if voice.id == "pl-PL":
        polish_voice_index = i
        

if polish_voice_index is not None:
    print('pl-PL')
    engine.setProperty('voice', voice[polish_voice_index].id)


# Funkcja do nasłuchiwania i rozpoznawania mowy
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Słucham...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Rozpoznawanie...")
            query = r.recognize_google(audio, language='pl-PL')
            print(f"Zrozumiałem: {query}")
        except Exception as e:
            print("Przepraszam, nie rozpoznano.")
            return "None"
        return query

# Funkcja do przetwarzania i odpowiedzi na pytanie
def response(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Główna pętla programu
while True:
    query = listen().lower()
    
    if "cześć" in query:
        response("Cześć! W czym mogę pomóc?")
    
    elif "jaka jest pogoda" in query:
        # Tutaj możesz dodać kod obsługujący zapytanie o pogodę za pomocą API
        response("Przepraszam, nie mam zaimplementowanej funkcji pobierania pogody.")
    
    elif "do widzenia" in query:
        response("Do widzenia!")
        break
