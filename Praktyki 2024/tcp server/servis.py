
import mysql.connector,socketserver,json,datetime
import socket
import sys
import win32serviceutil
import servicemanager
import win32event
import win32service


class SMWinservice(win32serviceutil.ServiceFramework):

    _svc_name_ = 'servistcp_python_name'
    _svc_display_name_ = 'servistcp_python_name_displayname'
    _svc_description_ = 'Jakos dziala'

    @classmethod
    def parse_command_line(cls):
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        self.proc = None
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False
        sys.exit()


    def main(self):
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

                blad = 0
                cursor = mydb.cursor()
                self.ip = self.client_address[0]
                self.data = self.request.recv(1024).strip()

                query = "SELECT * FROM skanery WHERE ip = %s"
                cursor.execute(query, (self.ip,))
                result = cursor.fetchone()

                query = "select DISTINCT a.idArtykul from artykul a  JOIN skany s on LEFT(s.kod, 4) = RIGHT(a.Indeks, 4) WHERE s.kod = %s"
                cursor.execute(query, (self.data,))
                result2 = cursor.fetchone()

                if result2 is not None:
                    wynik = f"{self.ip}", int(self.data), result2[0],datetime.datetime.now(),blad
                else:
                    blad = 1
                    wynik = f"{self.ip}", int(self.data), None,datetime.datetime.now(),blad

                print(len(str(int(self.data))))

                if len(str(int(self.data))) == 18:
                    blad = 1

                if result:
                    print("IP Address exists in the database")
                    query="insert into skany (ip, kod, idArtykul,data,blad) values (%s, %s,%s,%s,%s)"
                    print(query,wynik)
                    cursor.execute(query, wynik)
                    mydb.commit()
                else:
                    print("IP Address does not exist in the database")
                    blad = 'błąd'  # Ustawienie zmiennej błąd

                try:
                    index = str(int(self.data))[0:4]
                    query = "SELECT nazwa FROM artykul a WHERE RIGHT(CAST(indeks AS CHAR), 4) = %s"
                    cursor.execute(query, (index,))
                    result = cursor.fetchone()
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
                    filepath = 'C:/Users/xxx/Baza danych/python/Praktyki 2024/tcp server/output.json'
                    with open(filepath, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                    data.append(result_to_save)
                    with open(filepath, 'w', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                except:
                    print("błąd")

        def server():
            HOST, PORT = "10.2.1.63", 8555

            with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
                server.serve_forever()
        server()

if __name__ == '__main__':
    SMWinservice.parse_command_line()
