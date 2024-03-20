
import mysql.connector,socketserver,json,datetime
class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # próba połączenia z bazą danych
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="toor",
                password="ZAQ!2wsx",
                database="skany_base"
            )
        except:
            pass
        blad = 0
        cursor = mydb.cursor()
        self.ip = self.client_address[0]
        self.data = self.request.recv(1024).strip()

        # czy jest adres ip
        query = "SELECT * FROM skanery WHERE ip = %s"
        cursor.execute(query, (self.ip,))
        result = cursor.fetchone()

        # zapytanie SQL do pobrania id artykułu na podstawie kodu skanu
        query = "select DISTINCT a.idArtykul from artykul a  JOIN skany s on LEFT(s.kod, 4) = RIGHT(a.Indeks, 4) WHERE s.kod = %s"
        cursor.execute(query, (self.data,))  # Wykonywanie zapytania
        result2 = cursor.fetchone()  # Pobieranie wyniku zapytania

        # Sprawdzanie, czy wynik zapytania jest pusty
        if result2 is not None:
            wynik = f"{self.ip}", int(self.data), result2[0],datetime.datetime.now(),blad  # Przygotowywanie wyniku
        else:
            blad = 1
            wynik = f"{self.ip}", int(self.data), None,datetime.datetime.now(),blad  # Przygotowywanie wyniku
        print(len(str(int(self.data))))  # Wydrukowanie długości danych

        if len(str(int(self.data))) == 18:
            blad = 1
        # Sprawdzanie, czy wynik zapytania istnieje i czy długość danych wynosi 18
        if result:
            print("IP Address exists in the database")  # Wydrukowanie informacji, że adres IP istnieje w bazie danych
            query="insert into skany (ip, kod, idArtykul,data,blad) values (%s, %s,%s,%s,%s)"  # Przygotowanie zapytania SQL
            print(query,wynik)  # Wydrukowanie zapytania SQL i wyniku
            cursor.execute(query, wynik)  # Wykonywanie zapytania SQL
            mydb.commit()  # Zatwierdzanie transakcji
        else:
            print("IP Address does not exist in the database")  # Wydrukowanie informacji, że adres IP nie istnieje w bazie danych
            blad = 'błąd'  # Ustawienie zmiennej błąd
        
        
        
        
        
        
        
        
        
        def logi():
            try:
                index = str(int(self.data))[0:4]  # Wyodrębnienie indeksu
                query = "SELECT nazwa FROM artykul a WHERE RIGHT(CAST(indeks AS CHAR), 4) = %s"  # Przygotowanie zapytania SQL
                cursor.execute(query, (index,))  # Wykonywanie zapytania SQL
                result = cursor.fetchone()  # Pobieranie wyniku zapytania
                data = str(int(self.data))  # Konwersja danych na string
                if blad:
                    data = "Error"  # Ustawienie danych na "Error", jeśli wystąpił błąd
                    blad = None  # Resetowanie zmiennej błąd
            
                # Przygotowanie wyniku do zapisu
                result_to_save = {
                                'index': index,
                                'data': data,
                                'time': str(datetime.datetime.now()),
                                'result': result[0].replace('"', "'") if result else ''
                                }
                filepath = 'C:/Users/xxx/Baza danych/python/Praktyki 2024/tcp server/output.json'  # Ścieżka do pliku
                with open(filepath, 'r', encoding='utf-8') as file:  # Otwarcie pliku do odczytu
                    data = json.load(file)  # Wczytanie danych z pliku

                data.append(result_to_save)  # Dodanie wyniku do wczytanych danych

                with open(filepath, 'w', encoding='utf-8') as file:  # Otwarcie pliku do zapisu
                    json.dump(data, file, ensure_ascii=False, indent=4)  # Zapis danych do pliku


            except:
                print("błąd")  # Wydrukowanie informacji o błędzie






def server():
    HOST, PORT = "10.2.1.63", 8555  # Ustawienie hosta i portu

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:  # Tworzenie serwera
        server.serve_forever()  # Uruchomienie serwera


server()  # Wywołanie funkcji server

