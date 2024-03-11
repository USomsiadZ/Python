from cvzone.HandTrackingModule import HandDetector
import cv2

# Inicjalizacja klasyfikatora kaskadowego Haar do wykrywania twarzy
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicjalizacja klasyfikatorów kaskadowych Haar do wykrywania oczu
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Inicjalizacja kamery
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
success, img = cap.read()
h, w, _ = img.shape
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    # Pobranie klatki z kamery
    success, img = cap.read()
    
    # Wykrywanie twarzy
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        # Narysuj prostokąt wokół twarzy
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # Wykrywanie oczu
        roi_gray = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 0, 0), 2)
    
    # Wykrywanie rąk i ich punktów charakterystycznych
    hands, img = detector.findHands(img)  # z rysowaniem
    # hands = detector.findHands(img, draw=False)  # bez rysowania

    # Wyświetlenie obrazu
    cv2.imshow("Obraz", img)
    if cv2.waitKey(1) == 27:
        break  # Naciśnij klawisz "Esc", aby zakończyć program

# Zwolnienie zasobów kamery i zamknięcie okna OpenCV
cap.release()
cv2.destroyAllWindows()
