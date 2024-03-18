import mysql.connector,socketserver,json,datetime
class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="toor",
                password="ZAQ!2wsx",
                database="skany_base"
            )
        except:
            pass
        blad = None
        cursor = mydb.cursor()
        self.ip = self.client_address[0]
        self.data = self.request.recv(1024).strip()
        wynik = f"{self.ip}",int(self.data)
        print(wynik)
        query = "SELECT * FROM skanery WHERE ip = %s"
        cursor.execute(query, (self.ip,))
        result = cursor.fetchone()
        print(len(str(int(self.data))) )
        if result and len(str(int(self.data))) == 18:
            print("IP Address exists in the database")
            query="insert into skany (ip, kod) values (%s, %s)"
            cursor.execute(query, wynik)
            mydb.commit()
        else:
            print("IP Address does not exist in the database")
            blad = 'błąd'
        try:
            index = str(int(self.data))[0:4]
            query = "SELECT nazwa FROM artykul a WHERE RIGHT(CAST(indeks AS CHAR), 4) = %s"
            cursor.execute(query, (index,))
            result = cursor.fetchone()
            print(result)
            data = str(int(self.data))
            if blad:
                data = "Error"
                blad = None
            
            result_to_save = {
                               'index': index,
                               'data': data,
                               'time': str(datetime.datetime.now()),
                               'result': result[0].replace('"', "'") if result else ''
                             }
            with open('C:/Users/xxx/Baza danych/python/Praktyki 2024/tcp server/Logi-GUI-C#/logi-gui/output.json', 'a', encoding='utf-8') as file:
                file.write(json.dumps(result_to_save, ensure_ascii=False))
                file.write("\n")   # To ensure each log is on a new line
        except:
            print("błąd")


        



def server():
    HOST, PORT = "10.2.1.63", 8555

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()


server()



