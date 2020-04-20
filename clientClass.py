import socket
import sys
import time
import os
import struct

CRLF = "\r\n"

class Client: 

    # Define Class Variables: 

    RepresenationType = "A"; # Ascii 
    RepresentationTypeControl = "N" # Non-Print
    FileStructure = "F" # File 
    TransferMode = "S" # Stream 

    ControlPort = 21
    DataPort = 1232 # Calculate dataport with {port = p1*256+p2}. 
    # What is P1 and P2? 
    #  4 * 256 = 1024
    # 1232 - 1024 = 208
    # P1 = 4 and P2 = 208 
    P1 = "4"
    P2 = "208"
        
    #Define Class Methods: 

    def __init__(self, ServerIPAddr):
        self.Host = ServerIPAddr
        self.Addr = self.Host.replace(".", ",")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.datasocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.datasocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def Run(self): 

        print("Starting connection to server: ....")

        result = self.client.connect_ex((self.Host, self.ControlPort))

        if result == 0:
            print ("Port is open")
            Data = self.client.recv(4096)
            Data = Data.decode("utf-8")
            Code = Data[0:3]
            if Code == "": 
                print("No code received")
            else: self.Codes(Code)
                        # client.close()   

        else:
            print ("Port is not open")


    def Codes(self, Code):
  
        if Code == '150':
            print("File status okay")
            return True

        if Code == '200':
            print("Server Okay")
            return True

        if Code == '220':
            print("Server Ready for new user")
            self.login()
            return True

        if Code == '226':
            print("File Transfer Succesful")
            self.datasocket.close()
            return True
            
        if Code == '230':
            print("Password Correct")
            return True

        if Code == '332':
            print("before login")
            self.login()
            return True

        if Code == '331':
            print("Correct Username")
            return True 

        if Code == '530':
            print("Incorrect Username or Password")
            return False


    def login(self):

        while True:
            print("Username: ")
            Username = input()
            self.USER(Username)
            Code = self.receiveCode()
            check = self.Codes(Code)
            print(check)
            if check == True: break
        
        while True:
            print("Password: ")
            Password = input()
            self.PASS(Password)
            Code = self.receiveCode()
            check = self.Codes(Code)
            if check == True: break

    def sendCmd (self, cmd): # add CRLF here so don't have to do it all the time
        toSend = cmd + CRLF
        self.client.send(bytes(toSend,"utf-8"))

    def receiveCode (self): 
        received = self.client.recv(4096)
        received = received.decode("utf-8")
        print(received[0:3])
        return received[0:3]

    def USER(self, name):
        send = "USER " + name
        self.sendCmd(send)

    def PASS(self, pWord):   
        send = "PASS " + pWord
        self.sendCmd(send)

    def PORT(self):
        print("PORT")
        string = "PORT " + self.Addr + "," + self.P1 + "," + self.P2 # our dataport is just an 8bit nunber?
        self.sendCmd(string)
        Check = self.Codes(self.receiveCode())
        if Check == True: return True 
        print("OUTOFPORT")

    def connect_datasocket(self):
        # PORT()
        self.datasocket.bind((self.Host, self.DataPort))
        self.datasocket.listen(5)
        print("ACCEPTED DATASOCKET")

    def STOR(self, filePath, fileName): # server to accept and store data - if file exists it overwrites, new file created if not
        print("In STOR now...)")
        check = self.PORT()
        if check == False: return False 
        toSend = "STOR " + fileName
        self.sendCmd(toSend)
        self.connect_datasocket()
        # Going to be receiving some codes here: 
        code = self.receiveCode()
        check = self.Codes(code)
        if check == False: return 
        while True:   
            serv, addr = self.datasocket.accept()
            print(addr)
            file = open(filePath,'r')
            upload = file.read(4096)
            while upload: 
                print(upload)
                serv.send(upload) # HELP! Should this be serv.send? See connect_datasock...fxn
                upload = file.read(4096)
            break
        file.close()
        code = self.receiveCode()
        check = self.Codes(code)

    def RETR(self, path): #This function should send the retr command as well as open up a new file to write the downloaded data into 
        # Connect to dataport: call fxn 
        self.connect_datasocket()
        toSend = "RETR " + path 
        self.sendCmd(toSend)
        # Going to be receiving some codes here: 
        # code = receiveCode()
        # check = Codes(code)
        # if check == False: Break?  
        code = self.receiveCode()
        check = self.Codes(code)
        if check == False: return 

        #Might need to do some checks here that the connection is open or something? 
        #Open new file, download file with pathname 'path, write to newfile, close file
       
        while True: 
            serv, addr = self.datasocket.accept()
            print(addr)   
            newFile = open(path,'w')
            downloaded = serv.recv(4096)
            while downloaded: 
                print(downloaded)
                newFile.write(downloaded)
                downloaded = serv.recv(4096)
            break
        newFile.close()
        code = self.receiveCode()
        check = self.Codes(code)




client = Client ("192.168.8.100")    
client.Run()
client.RETR("ClientFiles/testFile.txt") # "testFile.txt"

      
 