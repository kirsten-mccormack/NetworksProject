import socket
# py -3.7 FileTransferClient.py
#  ipconfig getifaddr en0

CRLF = "\r\n"
RepresenationType = "A"; # Ascii 
RepresentationTypeControl = "N" # Non-Print
FileStructure = "F" # File 
TransferMode = "S" # Stream 
Host = "192.168.8.100"
ControlPort = 21
Addr = Host.replace(".", ",")
DataPort = 1232 # Calculate dataport with {port = p1*256+p2}. 
# What is P1 and P2? 
#  4 * 256 = 1024
# 1232 - 1024 = 208
# P1 = 4 and P2 = 208 
P1 = "4"
P2 = "208"


def Codes(Code):
  
    if Code == '150':
        print("File status okay")
        return True

    if Code == '200':
        print("Server Okay")
        return True

    if Code == '220':
        print("Server Ready for new user")
        login()
        return True

    if Code == '226':
        print("File Transfer Succesful")
        datasocket.close()
        return True
        
    if Code == '230':
        print("Password Correct")
        return True


    if Code == '332':
        print("before login")
        login()
        return True

    if Code == '331':
        print("Correct Username")
        return True 

    if Code == '530':
        print("Incorrect Username or Password")
        return False
        

def login():
    while True:
        print("Username: ")
        Username = input()
        USER(Username)
        Code = receiveCode()
        check = Codes(Code)
        print(check)
        if check == True: break
    
    while True:
        print("Password: ")
        Password = input()
        PASS(Password)
        Code = receiveCode()
        check = Codes(Code)
        if check == True: break

    # connect_datasocket()
    # Code = receiveCode()
    # check = Codes(Code)
    # print(check)

    STOR("ClientFiles/testFile.txt", "testFile.txt")
    


def sendCmd (cmd): # add CRLF here so don't have to do it all the time
    toSend = cmd + CRLF
    client.send(bytes(toSend,"utf-8"))

def receiveCode (): 
    received = client.recv(4096)
    received = received.decode("utf-8")
    print(received[0:3])
    return received[0:3]

def USER(name):
  send = "USER " + name
  sendCmd(send)

def PASS(pWord):   
  send = "PASS " + pWord
  sendCmd(send)

def PORT():
    print("PORT")
    string = "PORT " + Addr + "," + P1 + "," + P2 # our dataport is just an 8bit nunber?
    sendCmd(string)
    Check = Codes(receiveCode())
    if Check == True: return True 
    print("OUTOFPORT")

def connect_datasocket():
    datasocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    datasocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # PORT()
    datasocket.bind((Host, DataPort))
    datasocket.listen(5)
    print("ACCEPTED DATASOCKET")
    return datasocket

def STOR(filePath, fileName): # server to accept and store data - if file exists it overwrites, new file created if not
    print("In STOR now...)")
    check = PORT()
    if check == False: return False 
    toSend = "STOR " + fileName
    sendCmd(toSend)
    datasocket = connect_datasocket()
    # Going to be receiving some codes here: 
    code = receiveCode()
    check = Codes(code)
    if check == False: return 
    while True:   
        serv, addr = datasocket.accept()
        print(addr)
        file = open(filePath,'r')
        upload = file.read(4096)
        while upload: 
            print(upload)
            serv.send(upload) # HELP! Should this be serv.send? See connect_datasock...fxn
            upload = file.read(4096)
        break
    file.close()
    code = receiveCode()
    check = Codes(code)
  

# Set up control socket 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.bind((Host,ControlPort))
result = client.connect_ex((Host, ControlPort))

if result == 0:
    print ("Port is open")
    Data = client.recv(4096)
    Data = Data.decode("utf-8")
    Code = Data[0:3]
    if Code == "": 
        print("No code received")
    else: Codes(Code)
    # client.close()   

else:
   print ("Port is not open")
