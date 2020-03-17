import socket
# py -3.7 FileTransferClient.py

def Codes(Code):
  if Code == '332':
    login()


def login():
  while True:
    print("Username: ")
    Username = input();
    Username = 'USER ' + Username
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

    Password = 'PASS ' + Password
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



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((socket.gethostname(), 1234))
result = client.connect_ex((socket.gethostname(), 1234))

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