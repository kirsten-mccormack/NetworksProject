import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from os import path
from api import Api

class ClientUI:

    FILES = [
        "file1",
        "file2",
        "file3"
    ]
    def __init__(self):
        self.window = tk.Tk()
        # Calls API so that a message is sent to server for connection to occur 
        # when connection is established get the screen with all the login and file transfer stuff
 
    def OpenWindow(self):
        # everything we need to show on the window (buttons, input boxes, menu etc) 
        self.window.title("AlKir's FTP client")
        self.window.geometry('500x400')
        # call a whole lot of stuff between here 
        self.WelcomeWindow()
        self.window.mainloop()
        # can call more fxns 

    def WelcomeWindow(self):
        # the window that will show at first saying welcome to the applicationa
        f = tk.Frame(self.window)
        f.grid(sticky="NESW")
        w = tk.Label(f, text="Welcome to my FTP client.")
        w.grid(row=0, column=1)
        # ask for server address 
        addressLbl = tk.Label(f, text="Server Address:")
        addressLbl.grid(row=4, column=2)
        # # # input box for username
        addressEntry = tk.Entry(f,width="12")
        addressEntry.grid(row=5, column=2)
        # # button to connect to server
        def connect():
            # print(addressEntry.get())
            api = Api(addressEntry.get())
            if (api.status == True): 
                self.clearFrame(f)
                # go to log in screen 
                self.loginScreen(api)
                #carry on to somewhere else 
            if (api.status == False): 
                messagebox.showinfo("Connection Error", "Failed to Connect to Server.\n Please try again.")
                addressEntry.delete(0, 'end')
        btn = tk.Button(f, text="Connect", command=connect, bg ='blue')
        btn.grid(row=6, column=2)
        # on click, must connect to API and send address to Server
        # if API.status = True go to log in screen 
        # else tell user to try reconnect to server  
      
   

    def OpenCurrentFile(self,fileOrPath):
        # The stuff to open the directory 
        print("Hello")
 
    def PopUp(self,message):
        # A pop up in case a file cannot be found or transfered
        messagebox.showinfo("Kickass FTP GUI", " Welcome to our project!")              #  Widgets go here apparently....

    def loginScreen(self, api):
        f = tk.Frame(self.window)
        f.grid()
        # login screen welcome message
        
        messageLbl = tk.Label(f, text="Please enter your account details:")
        messageLbl.grid(row="2", column="5")
        # text for username 
        userLbl = tk.Label(f, text="Username:")
        userLbl.grid(row="3", column="4")
        # input box for username
        nameEntry = tk.Entry(f,width=10)

        nameEntry.grid(row="3", column="5")

        passLbl = tk.Label(f, text="Password:")

        passLbl.grid(row="5", column="4")
        #input box for password 
        passEntry = tk.Entry(f, width=10)

        passEntry.grid(row="5", column="5")

        def login():
            # lbl.configure(text="Button was clicked !!")
            result = api.login(nameEntry.get(),passEntry.get())
            if (result == True): 
                print("Hello") #carry on to somewhere else 
                self.clearFrame(f)
                self.mainFrame(api)

            if (result == False): 
                error = tk.Label(f, text="Login Error! Failed to Login User. Please try again.")
                error.grid(row="6", column="5")
                nameEntry.delete(0, 'end')
                passEntry.delete(0, 'end')
            # login the user 


        btn = tk.Button(f, text="Log In", command=login, bg ='blue')
        btn.grid(row="7", column="5")

    def clearFrame(self, frame):
        # destroy all widgets from frame
        for widget in frame.winfo_children():
            widget.destroy()

        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        frame.pack_forget() 

    def mainFrame(self, api):
        f = tk.Frame(self.window)
        f.grid()
        # file input for retrieval 
        retrvLbl = tk.Label(f, text="Specify file for retrieval:")
        retrvLbl.grid(row=0, column=1)
        # browse for file 
        variable = StringVar(f)
        dropDown = OptionMenu(f, variable, *self.FILES)
        # dropDown = OptionMenu(f, variable, *api.getAllFiles())
        dropDown.grid(row=0, column=2)
        # retrieve button 
        def retrieve():
            # call the API file trieve and send the filename 
            # filepath = ? 
            #api.retrieve(filepath)
            print("retrieve file: " + variable.get())
            #  variable.get() currently returns the file name but it will depend on what is stored in the list, filenames or paths
            # where will we get the path to the file? 

        retrvBtn = tk.Button(f, text="Retrieve", command=retrieve, bg ='blue')
        retrvBtn.grid(row=0, column=3)
       
        # file input for sending 
        sendLbl = tk.Label(f, text="Specify file for sending:")
        sendLbl.grid(row=1, column=1)
        # browse for file 
        def browse():
            file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
            print("browsing for file")
            print("selected file: " + file)
            # file returns the file path 

        browseBtn = tk.Button(f, text="Browse", command=browse, bg ='blue')
        browseBtn.grid(row=1, column=2)
        # sending button
        def send():
            # send file
            # filename = ? # ask the user to name the file for storage? # the last part of the path after the last '/'?
            # filepath = file # path returned to the file they selected from the file browser
            # api.send(filename, filepath)
            print("send file: " + file.get())
        sendBtn = tk.Button(f, text="Send", command=send, bg ='blue')
        sendBtn.grid(row=1, column=3)
        # quit button -> closes window and breaks connection to server 
        # make sure the "x" button also breaks the connection
        # listen for responces from server and display in a popup 














































































































































































































































































































































































































































































# file = filedialog.askopenfilename()
# file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__))


# 

# b = tk.Button ( window , text = ' Hey Friend!!' , bg = "red", command = welcomeWindow )
# b.pack()

# C = tk.Canvas(window, bg="blue", height=250, width=300)
# coord = 10, 50, 240, 210
# arc = C.create_arc(coord, start=0, extent=150, fill="red")
# C.pack()

