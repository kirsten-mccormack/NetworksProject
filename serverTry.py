# To run this code from commandline: 
# python3 server.py

import socket
import sys
import time
import os
import struct


CRLF = "\r\n"

# Default for types
RepresenationType = "A"; # ASCII
RepresentationTypeControl = "N" # Non-Print
FileStructure = "F" # File 
TransferMode = "S" # Stream 

# Initialise the socket 
HOST = "192.168.8.106" # This local server
CONN_PORT = 21 # A random choice for connection port 
BUFFER_SIZE = 1024 # Standard size
DATA_PORT = 20
LoggedIn = False

DefaultClientDataAddress = ""
DefaultClientDataPort = 0 

def commands(Command):
#  Get th+e Command Name and the rest of the command
    IndexName = Command.find(" ")
    # print("Index " + IndexName)
    CommandName = Command[0:IndexName]
    print("Command " + CommandName)
    IndexRest = Command.find(CRLF)
    # If not found then maybe throw an exception 
    RestOfCommand = Command[IndexName+1:IndexRest]
    print("RestOfCommand " + CommandName)

    if CommandName == "PORT":
        PORT(RestOfCommand)
    if CommandName == "RETR":
        RETR(RestOfCommand)
    if CommandName == "STOR":
        STOR(RestOfCommand)
    if CommandName == "QUIT":
        QUIT()
    if CommandName == "NOOP":
        NOOP()

def SendCode(Code):
    client.send(Code)

def ReceiveData(size):
    return client.recv(size)

def login():
    while True:
        received = ReceiveData(4096)
        print(received)
        received = received.decode("utf-8")
        print("Received data: " + received)
        if ( received[0:4] == 'USER' ):
            username = received[5:-2]
            print(username)
            if ( username == "Alice" ):
                SendCode(bytes("331 Username OK" + CRLF,"utf-8"))
                print("Correct Username")
                break
            else: 
                SendCode(bytes("530 Not Logged In. Username Incorrect" + CRLF,"utf-8"))
        else: 
           SendCode(bytes("332 Account required for login" + CRLF,"utf-8"))

    while True:
        received = ReceiveData(4096)
        received = received.decode("utf-8")
        print("Received data: " + received)
        if ( received[0:4] == 'PASS' ):
            print(received[0:4])
            password = received[5:-2]
            print(password)
            if ( password == "Kirsten" ):
                client.send(bytes("230 Password OK\r\n","utf-8"))
                break
            else: 
                client.send(bytes("530 Not Logged In. Password Incorrect\r\n","utf-8"))

        else: 
           client.send(bytes("331 Username OK. Password required.\r\n","utf-8"))
    
    LoggedIn = True
        

def PORT(RestOfCommand):
    print("PORT")
    GetAddrPort = RestOfCommand
    #Ensure that it is in the correct format

    IndexFound = -1

    for x in range(4):
        IndexFound = GetAddrPort.find(",",IndexFound+1)

    Client_DataAddr = GetAddrPort[0:IndexFound].replace(",",".")

    GetAddrPort = GetAddrPort[IndexFound+1:]
    Ports = GetAddrPort.split(",")

    P1 = int(Ports[0])
    P2 = int(Ports[1])
    Client_DataPort = P1*256+P2
    
    SendCode(bytes("200 Okay","utf-8"))

def MAKEDATACONN():
    #Make data connection and return if it worked or not 
    # Check if it is a reliable port number 
    data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    data.bind((HOST,DATA_PORT))
    result = client.connect_ex((Client_DataAddr, Client_DataPort))

    if result == 1:
        Client_DataPort = DefaultClientDataPort
        result = client.connect_ex((Client_DataAddr, Client_DataPort))

        if result == 1:
            return 0

    return 1

def STOR(Pathname):
   # 
    print("Hello")

def RETR():
    # 
    print("Hello")

def QUIT():
    LoggedIn = False
    client.close()
    
def NOOP():
    SendCode(bytes("200 OKAY" + CRLF ,"utf-8"))

def close():
    try: serv.shutdown(socket.SHUT_RDWR) #socket.SHUT_RDWR
    except (socket.error, OSError, ValueError):
        pass
    serv.close()
    print ("closed")
    return True

print ("FTP Server...\n")

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Apparently this is necessary to make the port reusable again after closing
serv.bind((HOST, CONN_PORT))
serv.listen(5)

while True: 
    print ("Waiting for connection from client...\r\n")
    client, addr = serv.accept()
    client.send(bytes("220 Server ready for new user\r\n","utf-8"))
    DefaultClientDataAddress = addr[0]
    DefaultClientDataPort = addr[1]

    Client_DataAddr = DefaultClientDataAddress
    Client_DataPort = DefaultClientDataPort
    
    login()
    data = ReceiveData(1024).decode("utf-8")
    commands(data)
    CLOSED = close()
    if CLOSED == True:
        break

    # // This is the code to interface with the FileZilla Client: 
    # data = client.recv(4096);
    # print(data)
    # client.send(bytes("500 Security something\r\n","utf-8"))
    # data = client.recv(4096);
    # print(data)
    # client.send(bytes("500 Security something\r\n","utf-8"))
    # login()


    # while true:
    # filename = input(str("Please enter the filename: "))
    # file = open(filename,"rb")
    # file_data = file.read(1024)

    # client.send(file_data)
    # print ("Data succesfully transmitted. /n")


# print ("\nConnected to by address: {}".format(addr))

# define min commands: 
#                    USER, QUIT, PORT,
#                    TYPE, MODE, STRU, for the default values
#                    RETR, STOR, NOOP

#def stor():
#            This command causes the server-DTP to accept the data
#           transferred via the data connection and to store the data as
#            a file at the server site.  If the file specified in the
#            pathname exists at the server site, then its contents shall
#            be replaced by the data being transferred.  A new file is
#            created at the server site if the file specified in the
#            pathname does not already exist.

#def noop():
#            This command does not affect any parameters or previously
#            entered commands. It specifies no action other than that the
#            server send an OK reply.

# def retr():
#            This command causes the server-DTP to transfer a copy of the
#            file, specified in the pathname, to the server- or user-DTP
#            at the other end of the data connection.  The status and
#            contents of the file at the server site shall be unaffected.

# def stru():
#            The argument is a single Telnet character code specifying
#            file structure described in the Section on Data
#            Representation and Storage.
#            The following codes are assigned for structure:
#               F - File (no record structure)
#               R - Record structure
#               P - Page structure
#            The default structure is File.

# def mode():
#            The argument is a single Telnet character code specifying
#            the data transfer modes described in the Section on
#            Transmission Modes.
#            The following codes are assigned for transfer modes:
#               S - Stream
#               B - Block
#               C - Compressed
#            The default transfer mode is Stream.

# def type():
#     The argument specifies the representation type as described
#            in the Section on Data Representation and Storage.  Several
#            types take a second parameter.  The first parameter is
#            denoted by a single Telnet character, as is the second
#            Format parameter for ASCII and EBCDIC; the second parameter
#            for local byte is a decimal integer to indicate Bytesize.
#            The parameters are separated by a <SP> (Space, ASCII code 32).
#            The following codes are assigned for type:
#                         \    /
#               A - ASCII |    | N - Non-print
#                         |-><-| T - Telnet format effectors
#               E - EBCDIC|    | C - Carriage Control (ASA)
#                        /    \
#               I - Image
#               L <byte size> - Local byte Byte size

# def port():
#    The argument is a HOST-PORT specification for the data port
#            to be used in data connection.  There are defaults for both
#            the user and server data ports, and under normal
#            circumstances this command and its reply are not needed.  If
#            this command is used, the argument is the concatenation of a
#            32-bit internet host address and a 16-bit TCP port address.
#            This address information is broken into 8-bit fields and the
#            value of each field is transmitted as a decimal number (in
#            character string representation).  The fields are separated
#            by commas.  A port command would be:
#               PORT h1,h2,h3,h4,p1,p2
#            where h1 is the high order 8 bits of the internet host
#            address.
