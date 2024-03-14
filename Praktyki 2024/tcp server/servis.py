import socket
import sys
import win32serviceutil
import servicemanager
import win32event
import win32service
import mysql.connector
import socketserver

class SMWinservice(win32serviceutil.ServiceFramework):
    '''Base class to create winservice in Python'''

    _svc_name_ = 'servistcp_python_name'
    _svc_display_name_ = 'servistcp_python_name_displayname'
    _svc_description_ = 'Jakos dziala'

    @classmethod
    def parse_command_line(cls):
        '''
        ClassMethod to parse the command line
        '''
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        self.proc = None
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        '''
        Called when the service is asked to stop
        '''
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        '''
        Called when the service is asked to start
        '''
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

            # Create the server, binding to localhost on port 9999
            with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
                # Activate the server; this will keep running until you
                # interrupt the program with Ctrl-C
                server.serve_forever()
        pass
        server()
        while True:
            pass

# entry point of the module: copy and paste into the new module
# ensuring you are calling the "parse_command_line" of the new created class
if __name__ == '__main__':
    SMWinservice.parse_command_line()
