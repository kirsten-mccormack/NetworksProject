import socket
# py -3.7 FileTransferClient.py

def Codes(Code):
  if Code == '332':
    print("before login")
    login()



def login():
  while True:
    print("Username: ")
    Username = input();
    Username = 'USER ' + Username + "\r\n" 
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
    Password = 'PASS ' + Password + "\r\n"
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
  datasocket.connect((host, data_port)) 


host = "192.168.8.106"
port = 1233
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((host, port))
result = client.connect_ex((host, port))

# set up data port? 
data_port = 1232 #this okay? 
client.data_port = data_port
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


