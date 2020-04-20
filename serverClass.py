import socket
import sys
import time
import os
import struct

class Server: 
    CRLF = "\r\n"

    # Default for types
    RepresenationType = "A"; # ASCII
    RepresentationTypeControl = "N" # Non-Print
    FileStructure = "F" # File 
    TransferMode = "S" # Stream 

    # Initialise the socket 
    # HOST = "192.168.8.106" # This local server
    CONN_PORT = 21 # A random choice for connection port 
    BUFFER_SIZE = 1024 # Standard size
    DATA_PORT = 20
    LoggedIn = False

    DefaultClientDataAddress = ""
    DefaultClientDataPort = 0 

    def __init__(self, ServerIPAddr):
            self.Host = ServerIPAddr
    
    def run():
            
        while True: 
            
                login()
                i = 0
                while i < 2:
                        print(i)
                        Somedata = ReceiveData(1024).decode("utf-8")
                        print(Somedata)
                        if Somedata:
                        commands(Somedata)
                        i = i+1

                CLOSED = close()
                if CLOSED == True:
                        break

    def connectsocket():
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Apparently this is necessary to make the port reusable again after closing
        self.serv.bind((self.Host, self.CONN_PORT))
        self.serv.listen(5)
    
    def connect():
        self.connectsocket()

        print ("Waiting for connection from client...")
        self.client,ClientAddress = self.serv.accept()
        self.SendCode("220")
        
        self.DefaultClientDataAddress = ClientAddress[0]
        self.DefaultClientDataPort = ClientAddress[1]

        self.Client_DataAddr = self.DefaultClientDataAddress
        self.Client_DataPort = self.DefaultClientDataPort
        # Try and Error
    
    def commands(self, Command):
    #  Get th+e Command Name and the rest of the command
        IndexName = Command.find(" ")
        # print("Index " + IndexName)
        CommandName = Command[0:IndexName]
        print("Command " + CommandName)
        IndexRest = Command.find(CRLF)
        # If not found then maybe throw an exception 
        RestOfCommand = Command[IndexName+1:IndexRest]
        print("RestOfCommand " + RestOfCommand)

        if CommandName == "PORT":
        self.PORT(RestOfCommand)
        if CommandName == "RETR":
        self.RETR(RestOfCommand)
        if CommandName == "STOR":
        self.STOR(RestOfCommand)
        if CommandName == "QUIT":
        self.QUIT()
        if CommandName == "NOOP":
        self.NOOP()

    def SendCode(self, Code):

        StringToSend = ""

        if Code == "150":
        StringToSend = "150 File status okay; about to open data connection."
        if Code == "200":
        StringToSend = "200 Command okay."
        if Code == "220":
        StringToSend = "220 Service ready for new user."
        if Code == "226":
        StringToSend = "226 Closing data connection. Requested file transfer successful."
        if Code == "230":
        StringToSend = "230 User logged, proceed."
        if Code == "331":
        StringToSend = "331 User name okay, need password."
        if Code == "332":
        StringToSend = "332 Need account for login."
        if Code == "530":
        StringToSend = "530 Not logged in."

        self.client.send(bytes(StringToSend + self.CRLF,"utf-8")

    def ReceiveData(self,ServerConnection,size):
        # Check the received has CRLF at the end if not - bad command
        return ServerConnection.recv(size).decode("utf-8")

    def login(self):
        # If incorrect three times = Server disconnect
        # Make sure that logged in
        # Client logs in using different password server must disconnect from client
        self.USER()
        self.PASS()
        self.LoggedIn = True
            
    def USER():
        while True:
            received = self.ReceiveData(self.client, 4096)
            print(received)
            print("Received data: " + received)
            if (received[0:4] == 'USER' ):
                    username = received[5:-2]
                    print(username)
                    if (username == "Alice" ):
                        self.SendCode("331")
                        print("Correct Username")
                        break
                    else: 
                        self.SendCode("530")
            else: 
                self.SendCode("332")

    def PASS():
        while True:
            received = self.ReceiveData(self.client, 4096)
            print("Received data: " + received)
            if ( received[0:4] == 'PASS' ):
                print(received[0:4])
                password = received[5:-2]
                print(password)
                if (password == "Kirsten"):
                    self.SendCode("230")
                    break
                else: 
                    self.SendCode("530")

            else: 
                self.SendCode("331")

    def PORT(self,RestOfCommand):
        print("PORT")
        GetAddrPort = RestOfCommand
        #Ensure that it is in the correct format

        IndexFound = -1

        for x in range(4):
            IndexFound = GetAddrPort.find(",",IndexFound+1)

        self.Client_DataAddr = GetAddrPort[0:IndexFound].replace(",",".")

        GetAddrPort = GetAddrPort[IndexFound+1:]
        Ports = GetAddrPort.split(",")

        P1 = int(Ports[0])
        P2 = int(Ports[1])
        self.Client_DataPort = P1*256+P2
        print(self.Client_DataPort)
        
        SendCode("200")

    def MAKEDATACONN(self):
        #Make data connection and return if it worked or not 
        # Check if it is a reliable port number 
        print("IN MAKEDATACONN")
        data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        data.bind((self.Host,self.DATA_PORT))
        print(self.Client_DataAddr)
        print(self.Client_DataPort)

        if (self.Client_DataPort != self.DefaultClientDataPort) and (self.Client_DataAddr != self.DefaultClientDataAddress):
            result = data.connect_ex((self.Client_DataAddr, self.Client_DataPort))
            print(result)
        else: result == 0

        if result == 0:
        result = client.connect_ex((self.DefaultClientDataAddress, self.DefaultClientDataPort))
        print("CONNECTION NOT MADE 1") 

        if result == 0:
            print("CONNECTION NOT MADE 2")
            self.close()
            return data, 0

        print("CONNECTION MADE")
        return data, 1

    def STOR(self, Pathname):
        print("IN STOR")
        file = open(Pathname,'w')
        DataError = self.MAKEDATACONN()
        self.SendCode("150")
        print("AFTER FILE OPEN")
        # Check if file is open
        # Check the parameters are in the correct format and that there are parameters
        if DataError[1] == 0:
            # Send some error code
            print("Sad")
        else: #NEED SOMETHING HERE 

        while True: 
                data = DataError[0]
                downloaded = self.ReceiveData(data, 4096)
                print(downloaded)
                if not downloaded: break 
                file.write(downloaded)
                print("IN FILE WRITE")
                # Check and Open a file
                # Print some Error Code (150)
                # Receive data until complete
                # Print some Error Code (226)
                # Close data connection

        file.close()
        self.SendCode("226")
        data.close()
        print("END OF STOR")


    def RETR(self, pathname):
        # 
        print("Hello")

    def QUIT(self):
        self.LoggedIn = False
        client.close()
            
    def NOOP(self):
        self.SendCode("200")

    def close(self):
        self.client.close()
        try: serv.shutdown(socket.SHUT_RDWR) #socket.SHUT_RDWR
        except (socket.error, OSError, ValueError):
                pass
        serv.close()
        print ("closed")
        return True


server = Server("192.168.8.100")
server.run()