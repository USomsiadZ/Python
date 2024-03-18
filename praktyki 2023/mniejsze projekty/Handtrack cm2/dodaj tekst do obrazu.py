import cv2
import numpy as np
import speech_recognition as sr
import threading

# Inicjalizacja kamery
cap = cv2.VideoCapture(0)

# Inicjalizacja koloru tekstu
text_color = (255, 255, 255)

# Inicjalizacja rozpoznawania mowy
recognizer = sr.Recognizer()

# Ustawienie języka na polski w konfiguracji rozpoznawania
recognizer.energy_threshold = 4000  # Dostosuj próg na swoje potrzeby
recognizer.dynamic_energy_threshold = True
recognizer.operation_timeout = 5

# Funkcja do wyświetlania obrazu z tekstem
def display_image_with_text():
    global recognized_text
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Błąd odczytu klatki z kamery")
            break

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = text_color
        font_thickness = 2

        cv2.putText(frame, recognized_text, (10, 50), font, font_scale, font_color, font_thickness, lineType=cv2.LINE_AA)

        cv2.imshow("Obraz z tekstem", frame)

        key = cv2.waitKey(1)
        if key & 0xFF == 27:  # Przerwij pętle po wciśnięciu "Esc"
            break

    cap.release()
    cv2.destroyAllWindows()

# Funkcja do rozpoznawania mowy z mikrofonu
def recognize_speech():
    global recognized_text

    while True:
        with sr.Microphone() as source:
            print("Mów teraz...")
            audio = recognizer.listen(source, timeout=10)  # Timeout na 10 sekund

        try:
            recognized_text = recognizer.recognize_google(audio, language="pl-PL")  # Ustaw język na polski
            print("Rozpoznany tekst:", recognized_text)
        except sr.UnknownValueError:
            print("Nie rozpoznano mowy")
        except sr.RequestError as e:
            print("Błąd podczas rozpoznawania mowy: {0}".format(e))

# Rozpocznij obie wątki jednocześnie
recognized_text = ""
image_thread = threading.Thread(target=display_image_with_text)
speech_thread = threading.Thread(target=recognize_speech)

image_thread.start()
speech_thread.start()

image_thread.join()
speech_thread.join()
