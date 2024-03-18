import mysql.connector,socketserver
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
        cursor = mydb.cursor()
        self.ip = self.client_address[0]
        self.data = self.request.recv(1024).strip()
        wynik = f"{self.ip}",int(self.data)
        print(wynik)
        query = "SELECT * FROM skanery WHERE ip = %s"
        cursor.execute(query, (self.ip,))
        result = cursor.fetchone()

        if result:
            print("IP Address exists in the database")
            query="insert into skany (ip, kod) values (%s, %s)"
            cursor.execute(query, wynik)
            mydb.commit()
        else:
            print("IP Address does not exist in the database")



def server():
    HOST, PORT = "10.2.1.63", 8555

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()


server()


