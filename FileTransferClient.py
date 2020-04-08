import socket
# py -3.7 FileTransferClient.py
#  ipconfig getifaddr en0

CRLF = "\r\n"
RepresenationType = "A"; # Ascii 
RepresentationTypeControl = "N" # Non-Print
FileStructure = "F" # File 
TransferMode = "S" # Stream 
Host = "192.168.0.161"
Port = 1233
Addr = host.replace(".", ",")
DataPort = 1232 # Calculate dataport with {port = p1*256+p2}. 
# What is P1 and P2? 
#  4 * 256 = 1024
# 1232 - 1024 = 208
# P1 = 4 and P2 = 208 
P1 = 4
P2 = 208


def Codes(Code):
  if Code == '332':
    print("before login")
    login()
  
  if Code == '200':
    print("Server Okay")


def login():
  while True:
    print("Username: ")
    Username = input();
    Username = 'USER ' + Username + CRLF
    client.send(bytes(Username,"utf-8"))

    Data = client.recv(4096)
    Data = Data.decode("utf-8")
    Code = Data[0:3]

    if Code == '331':
        print("Correct Username")
        break
    elif Code == '530':
      print("Incorrect Username")
    else:
      Codes(Code)
      break
    
  while True:
    print("Password: ")
    Password = input();
    Password = 'PASS ' + Password + CRLF
    client.send(bytes(Password,"utf-8"))

    Data = client.recv(4096)
    Data = Data.decode("utf-8")
    Code = Data[0:3]

    if Code == '230':
      print("Password Correct")
      break
    elif Code == '530':
      print("Incorrect Password")
    else:
      Codes(Code)
      break
  

  # print("Password: ")
  # Password = 'PASS ' + Password
  # client.send(bytes(Password,"utf-8"))

def connect_datasocket():
  datasocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  PORT()
  datasocket.bind((HOST, DataPort))
  datasocket.listen(5)
  serv, addr = datasocket.accept()

def sendCmd (cmd)
  client.send(bytes(cmd,"utf-8"))

def receiveCode (): 
    received = client.recv(4096)
    return received[0:2]

def NOOP():
  # command does nothing but wait for okay reply 
  sendCmd("NOOP" + CRLF)
  Codes(receiveCode())

def PORT():
  string = "PORT " + Addr + "," + P1 + "," + P2 + CRLF # our dataport is just an 8bit nunber?
  sendCmd(string)
  Codes(receiveCode())

def RETR():



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((host, port))
result = client.connect_ex((host, port))

# set up data port? 
client.data_port = DataPort
# Connect to dataport: call fxn 
connect_datasocket()

if result == 0:
    print ("Port is open")

    Data = client.recv(4096)
    Data = Data.decode("utf-8")
    Code = Data[0:3]
    if Code == '220':
        print("Received Code")
        login()
    else:
      print ("Code Not Received")
    
    client.close()   

else:
   print ("Port is not open")


#    while True:
#         print("Enter data to send: ")
#         data = input()
#         client.send(bytes(data,"utf-8"))
#         from_server = client.recv(4096)
#         if data == "stop": break
#         print("Echo: " + from_server.decode("utf-8") + "\n")

#     client.close()   


