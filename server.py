# To run this code from commandline: 
# python3 server.py

import socket
import sys
import time
import os
import struct

def login():
    received = client.recv(4096)
    if ( received[0:4] == 'USER' ):
        print(received)
        username = received[6:-1]
        if ( username == "Alice" ):
            client.send(bytes("331 Username OK"))
    return

print ("FTP Server...\n")

# Initialise the socket 
HOST = socket.gethostname() # This local server
PORT = 1456 # A random choice
BUFFER_SIZE = 1024 # Standard size
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((HOST, PORT))
serv.listen(5)

print ("Waiting for connection from client...\n")
client, addr = serv.accept()
client.send("220 Server ready for new user")
login()
# print ("\nConnected to by address: {}".format(addr))

# while true:
#     filename = input(str("Please enter the filename: "))
#     file = open(filename,"rb")
#     file_data = file.read(1024)

#     client.send(file_data)
#     print ("Data succesfully transmitted. /n")


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
