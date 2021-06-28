## Client OS&NV 2021 Mensch ärgere dich nicht
#Import libraries
from tkinter import *
from tkinter import messagebox
import random
import socket
import pickle
import threading

#Initialize and set global variables
global num, dice_allowed, dice_force, count, your_turn
num = 0
dice_allowed = True
dice_force = True
count = True
your_turn = False

#create gamefield class
class canvas(Frame):
    def __init__(self, master=None):
        global count, your_turn
        super().__init__(master)
        self.round = 0
        #set field coordinates and colors
        self.coords = [(350, 75, 385, 110, '#FFFFFF'), (400, 75, 435, 110, '#FFFFFF'), (450, 75, 485, 110, '#819FF7'), (450, 160, 485, 125, 'white'), (450, 210, 485, 175, 'white'), (450, 260, 485, 225, 'white'), [450, 310, 485, 275, 'white'], (500, 310, 535, 275, 'white'), (550, 310, 585, 275, 'white'), (600, 310, 635, 275, 'white'), (650, 310, 685, 275, 'white'), (650, 360, 685, 325, 'white'), (650, 410, 685, 375, '#F2F5A9'), (600, 410, 635, 375, 'white'), (550, 410, 585, 375, 'white'), (500, 410, 535, 375, 'white'), (450, 410, 485, 375, 'white'), (450, 460, 485, 425, 'white'), (450, 510, 485, 475, 'white'), (450, 560, 485, 525, 'white'), (450, 610, 485, 575, 'white'), (400, 610, 435, 575, 'white'), (350, 610, 385, 575, '#F78181'), [350, 560, 385, 525, 'white'], (350, 510, 385, 475, 'white'), (350, 460, 385, 425, 'white'), (350, 410, 385, 375, 'white'), (300, 410, 335, 375, 'white'), (250, 410, 285, 375, 'white'), (200, 410, 235, 375, 'white'), (150, 410, 185, 375, 'white'), (150, 360, 185, 325, 'white'), (150, 310, 185, 275, '#81F781'), (200, 310, 235, 275, 'white'), (250, 310, 285, 275, 'white'), (300, 310, 335, 275, 'white'), (350, 310, 385, 275, 'white'), (350, 260, 385, 225, 'white'), (350, 210, 385, 175, 'white'), (350, 160, 385, 125, 'white'), (400, 560, 435, 525, '#F78181'), (400, 510, 435, 475, '#F78181'), (400, 460, 435, 425, '#F78181'), (400, 410, 435, 375, '#F78181'), (400, 160, 435, 125, '#819FF7'), (400, 210, 435, 175, '#819FF7'), (400, 260, 435, 225, '#819FF7'), (400, 310, 435, 275, '#819FF7'), (200, 360, 235, 325, '#81F781'), (250, 360, 285, 325, '#81F781'), (300, 360, 335, 325, '#81F781'), (350, 360, 385, 325, '#81F781'), (600, 360, 635, 325, '#F2F5A9'), (550, 360, 585, 325, '#F2F5A9'), (500, 360, 535, 325, '#F2F5A9'), (450, 360, 485, 325, '#F2F5A9'), (350, 75, 385, 110, '#FFFFFF'), (400, 75, 435, 110, '#FFFFFF'), (450, 75, 485, 110, '#819FF7'), (450, 160, 485, 125, 'white'), (450, 210, 485, 175, 'white'), (450, 260, 485, 225, 'white'), (450, 310, 485, 275, 'white'), (500, 310, 535, 275, 'white'), (550, 310, 585, 275, 'white'), (600, 310, 635, 275, 'white'), (650, 310, 685, 275, 'white'), (650, 360, 685, 325, 'white'), (650, 410, 685, 375, '#F2F5A9'), (600, 410, 635, 375, 'white'), (550, 410, 585, 375, 'white'), (500, 410, 535, 375, 'white'), (450, 410, 485, 375, 'white'), (450, 460, 485, 425, 'white'), (450, 510, 485, 475, 'white'), (450, 560, 485, 525, 'white'), (450, 610, 485, 575, 'white'), (400, 610, 435, 575, 'white'), (350, 610, 385, 575, '#F78181'), (350, 560, 385, 525, 'white'), (350, 510, 385, 475, 'white'), (350, 460, 385, 425, 'white'), (350, 410, 385, 375, 'white'), (300, 410, 335, 375, 'white'), (250, 410, 285, 375, 'white'), (200, 410, 235, 375, 'white'), (150, 410, 185, 375, 'white'), (150, 360, 185, 325, 'white'), (150, 310, 185, 275, '#81F781'), (200, 310, 235, 275, 'white'), (250, 310, 285, 275, 'white'), (300, 310, 335, 275, 'white'), (350, 310, 385, 275, 'white'), (350, 260, 385, 225, 'white'), (350, 210, 385, 175, 'white'), (350, 160, 385, 125, 'white'), (400, 560, 435, 525, '#F78181'), (400, 510, 435, 475, '#F78181'), (400, 460, 435, 425, '#F78181'), (400, 410, 435, 375, '#F78181'), (400, 160, 435, 125, '#819FF7'), (400, 210, 435, 175, '#819FF7'), (400, 260, 435, 225, '#819FF7'), (400, 310, 435, 275, '#819FF7'), (200, 360, 235, 325, '#81F781'), (250, 360, 285, 325, '#81F781'), (300, 360, 335, 325, '#81F781'), (350, 360, 385, 325, '#81F781'), (600, 360, 635, 325, '#F2F5A9'), (550, 360, 585, 325, '#F2F5A9'), (500, 360, 535, 325, '#F2F5A9'), (450, 360, 485, 325, '#F2F5A9')]
        self.master = master
        #set size and background color for window
        self.main_board = Canvas(self,width=800, height=700, bg = "#F5F6CE")
        self.main_board.pack()
        #recieve first message from server
        self.receive()
        #create new window for the dice
        self.newWindow = Toplevel(self.master)
        #force dice window to be at the front
        self.newWindow.after(1, lambda: self.newWindow.focus_force())
        #call Dice class
        Dice(self.newWindow)
        #set title for the gamefield window
        master.title("Mensch ärgere dich nicht!")
        self.pack()
        self.color = ""
    
    def new_window(self, event):
        global dice_allowed, dice_force, count, your_turn

        #If not players turn just receive
        if your_turn == False:
            self.receive()
            return

        self.caller = event.widget.find_withtag("current")[0]
        if dice_force == True:
            Dice(self.newWindow)
        
        #
        if count == False:
            your_turn = False
            dice_force = False
            dice_allowed = False
            self.send()
            return
        
        #If player must not dice
        if dice_allowed==False:
            y=list(self.coords[self.caller-1])
            if y[4]=="white":
                return
            self.clicked()
    
    #function to check where player clicked
    #and to decide what to do next depending on the colour of the field
    def clicked(self):
        global num,dice_allowed
        self.round +=1
        for j in range (0,5,1):
            for i in range (j+1,7,1):
                if ( self.caller == (40-j) and num == i):
                    y=list(self.coords[1+(i-j)])
                    y[4]="blue"
                    self.coords[1+(i-j)]=y
                    self.main_board.itemconfigure((i-j),fill="red")
                    print("you clicked:"+str(self.caller))
                    dice_allowed = True
                    self.main_board.itemconfigure(self.caller, fill = "white")
                    return
        y=list(self.coords[self.caller-1])
        for j in range (0,5,1):
            for i in range (1+j,7,1):
                if ((self.caller == 22-j) and (y[4] == "red") and (num >= j and num <= 4+j)):
                    y=list(self.coords[39+(num-j)])
                    y[4]="#F78181"
                    self.coords[39+(num-j)]=y
                    self.main_board.itemconfigure(40+(num-j),fill="red")
                    print("you clicked:"+str(self.caller))
                    dice_allowed = True
                    self.main_board.itemconfigure(self.caller, fill = "white")
                    return
        for j in range (0,5,1):
            for i in range (1+j,7,1):
                if ((self.caller == 32-j) and (y[4] == "green") and (num >= j and num <= 4+j)):
                    y=list(self.coords[47+(num-j)])
                    y[4]="#81F781"
                    self.coords[47+(num-j)]=y
                    self.main_board.itemconfigure(48+(num-j),fill="green")
                    print("you clicked:"+str(self.caller))
                    dice_allowed = True
                    self.main_board.itemconfigure(self.caller, fill = "white")
                    return
        for j in range (0,5,1):
            for i in range (1+j,7,1):
                if ((self.caller == 12-j) and (y[4] == "yellow") and (num >= j and num <= 4+j)):
                    y=list(self.coords[51+(num-j)])
                    y[4]="#F2F5A9"
                    self.coords[51+(num-j)]=y
                    self.main_board.itemconfigure(52+(num-j),fill="yellow")
                    print("you clicked:"+str(self.caller))
                    dice_allowed = True
                    self.main_board.itemconfigure(self.caller, fill = "white")
                    return
        for j in range (0,5,1):
            for i in range (1+j,7,1):
                if ((self.caller == 2-j) and (y[4] == "blue") and (num >= j and num <= 4+j)):
                    y=list(self.coords[43+(num-j)])
                    y[4]="#819FF7"
                    self.coords[43+(num-j)]=y
                    self.main_board.itemconfigure(44+(num-j),fill="blue")
                    print("you clicked:"+str(self.caller))
                    dice_allowed = True
                    self.main_board.itemconfigure(self.caller, fill = "white")
                    return
            
        if self.round == 1:
            y=list(self.coords[self.caller-1])
            if y[4] == "#F78181":
                self.color = "red"
            elif y[4] == "#819FF7":
                self.color = "blue"
            elif y[4] == "#F2F5A9":
                self.color = "yellow"
            else:
                self.color = "green"
                
        y=list(self.coords[self.caller+num-1])
        y[4] = self.color
        self.coords[self.caller+num-1]=y
        y=list(self.coords[self.caller-1])
        if y[0] == 450 and y[1] == 75:
            self.main_board.itemconfigure(self.caller, fill = "#819FF7")#
        elif y[0] == 650 and y[1] == 410:
            self.main_board.itemconfigure(self.caller, fill = "#F2F5A9")
        elif y[0] == 350 and y[1] == 610:
            self.main_board.itemconfigure(self.caller, fill = "#F78181")
        elif y[0] == 150 and y[1] == 310:
            self.main_board.itemconfigure(self.caller, fill = "#81F781")
        else:
            y[4]= "white"
            self.main_board.itemconfigure(self.caller, fill = "white")
        
        self.coords[self.caller-1]=y
        self.main_board.itemconfigure(self.caller+num,fill=self.color)
        print("you clicked:"+str(self.caller))
        self.send()
        dice_allowed = True

    def create_board(self):
        x0 = 0
        x1 = 0
        y0 = 0
        y1 = 0
        color = ""
        """
        ##Gamefield creation
        self.coords.append((350,75,385,110,"#FFFFFF"))
        self.coords.append((400,75,435,110,"#FFFFFF"))
        self.coords.append((450,75,485,110,"#819FF7"))#blue startfield
        for i in range(0,4,1):
            self.coords.append((450,160+((i)*50),485,125+((i)*50),"white"))
        for i in range(0,4,1):
            self.coords.append((500+((i)*50),310,535+((i)*50),275,"white"))
        self.coords.append((650,360,685,325,"white"))
        self.coords.append((650,410,685,375,"#F2F5A9"))#yellow startfield
        for i in range(1,4,1):
            self.coords.append((650-((i)*50),410,685-((i)*50),375,"white"))
        for i in range(0,4,1):
            self.coords.append((450,410+((i)*50),485,375+((i)*50),"white"))
        for i in range(0,2,1):
            self.coords.append((450-(50*i),610,485-(50*i),575,"white"))
        self.coords.append((350,610,385,575,"#F78181"))#red startfield
        for i in range(0,4,1):
            self.coords.append((350,560-(i*50),385,525-(i*50),"white"))
        for i in range(0,4,1):
            self.coords.append((300-((i)*50),410,335-((i)*50),375,"white"))
        self.coords.append((150,360,185,325,"white"))
        self.coords.append((150,310,185,275,"#81F781"))#green startfield
        for i in range(1,4,1):
            self.coords.append((150+((i)*50),310,185+((i)*50),275,"white"))
        for i in range(0,4,1):
            self.coords.append((350,310-(i*50),385,275-(i*50),"white"))
            
        for i in range(0,4,1):
            self.coords.append((400,560-((i)*50),435,525-((i)*50),"#F78181"))#red fields
        for i in range(0,4,1):
            self.coords.append((400,160+((i)*50),435,125+((i)*50),"#819FF7"))#blue fields
        for i in range(0,4,1):
            self.coords.append((200+((i)*50),360,235+((i)*50),325,"#81F781"))#green fields
        for i in range(0,4,1):
            self.coords.append((600-((i)*50),360,635-((i)*50),325,"#F2F5A9"))#yellow fields
        """

        for i in range (1,57,1):
            myTag = "{}".format(i)
            x0 = self.coords[i-1][0]
            y0 = self.coords[i-1][1]
            x1 = self.coords[i-1][2]
            y1 = self.coords[i-1][3]
            color = self.coords[i-1][4]
            field= self.main_board.create_oval(x0,y0,x1,y1,fill=color,tags=myTag)
            self.main_board.tag_bind(myTag, "<Button-1>", self.new_window)

    def send(self):
        global your_turn
        your_turn = False
        #send coordinates to server
        s.sendall(pickle.dumps(self.coords))
        print("sent")
        self.receive()
    
    #received data from server
    def receive(self):
        global your_turn
        received = s.recv(4096)
        #decode recieved data
        received_readable = pickle.loads(received)
        
        #If received message is a string
        if type(received_readable) == str:
            #Server tells player to start with its turn
            if received_readable == "TURN":
                your_turn = True
                self.create_board()
                
            #Server tells player another player has joined
            elif received_readable == "NEW":
                self.receive()
                
            #if any other message, do notinf
            else:
                your_turn = False
                
        #Server sent player new gamefield
        else:
            #players turn when received
            your_turn = True
            #update received coordinates 
            self.coords = received_readable
            #destroy old gamefield
            self.main_board.destroy()
            self.main_board = Canvas(self,width=800, height=700, bg = "#F5F6CE")
            self.main_board.pack()
            self.create_board()
            return

#create Dice class
class Dice:
    def __init__(self, master):
        #set size and Headline of the dice window
        self.master = master
        master.title("Würfel")
        master.geometry("200x180")
        self.play()
    
    #functionality of the dice
    def play(self):
        global dice_allowed
        self.frame = Frame(self.master)
        self.frame.pack()
        self.dice = Canvas(self.frame ,width=150, height=150, bg = "#F5F6CE")
        self.dice.pack()
        dice_allowed = True
        def roll_dice(event):
            global num, dice_allowed, dice_force, count
            while (dice_allowed == True):
                #If first round roll three times
                if num == 0:
                    for i in range (0,3,1):
                        print(i)
                        print("brr")
                        #delete current content from dice window
                        self.dice.delete("all")
                        #get random number
                        self.num = random.randint(1,6)
                        #draw dice depending on the rolled value
                        if self.num==1:
                            oval = self.dice.create_oval(70,70,85,85, fill="black")
                            dice_force = True
                        elif self.num==2:
                            oval = self.dice.create_oval(105,35,120,50, fill="black")
                            oval = self.dice.create_oval(50,105,35,120, fill="black")
                            dice_force = True
                        elif self.num==3:
                            oval = self.dice.create_oval(105,35,120,50, fill="black")
                            oval = self.dice.create_oval(50,105,35,120, fill="black")
                            oval = self.dice.create_oval(70,70,85,85, fill="black")
                            dice_force = True
                        elif self.num==4:
                            oval = self.dice.create_oval(105,35,120,50, fill="black")
                            oval = self.dice.create_oval(50,105,35,120, fill="black")
                            oval = self.dice.create_oval(105,105,120,120, fill="black")
                            oval = self.dice.create_oval(50,35,35,50, fill="black")
                            dice_force = True
                        elif self.num==5:
                            oval = self.dice.create_oval(105,35,120,50, fill="black")
                            oval = self.dice.create_oval(50,105,35,120, fill="black")
                            oval = self.dice.create_oval(105,105,120,120, fill="black")
                            oval = self.dice.create_oval(50,35,35,50, fill="black")
                            oval = self.dice.create_oval(70,70,85,85, fill="black")
                            dice_force = True
                        else: #6
                            oval = self.dice.create_oval(105,25,120,40, fill="black")
                            oval = self.dice.create_oval(50,115,35,130, fill="black")
                            oval = self.dice.create_oval(105,115,120,130, fill="black")
                            oval = self.dice.create_oval(50,25,35,40, fill="black")
                            oval = self.dice.create_oval(50,70,35,85, fill="black")
                            oval = self.dice.create_oval(105,70,120,85, fill="black")
                        if self.num == 6:
                            num = self.num
                            dice_force = False
                            return
                        
                        else:
                            #after rolling three times without a 6
                            if i == 2:
                                count = False
                                dice_allowed = False
                                return
                            continue
                
                #If not first round dice, draw dice depending on the rolled value
                else:
                    #delete current content from dice window
                    self.dice.delete("all")
                    #get random number
                    self.num = random.randint(1,6)
                    
                    #draw dice depending on the rolled value
                    if self.num==1:
                        oval = self.dice.create_oval(70,70,85,85, fill="black")
                    elif self.num==2:
                        oval = self.dice.create_oval(105,35,120,50, fill="black")
                        oval = self.dice.create_oval(50,105,35,120, fill="black")
                    elif self.num==3:
                        oval = self.dice.create_oval(105,35,120,50, fill="black")
                        oval = self.dice.create_oval(50,105,35,120, fill="black")
                        oval = self.dice.create_oval(70,70,85,85, fill="black")
                    elif self.num==4:
                        oval = self.dice.create_oval(105,35,120,50, fill="black")
                        oval = self.dice.create_oval(50,105,35,120, fill="black")
                        oval = self.dice.create_oval(105,105,120,120, fill="black")
                        oval = self.dice.create_oval(50,35,35,50, fill="black")
                    elif self.num==5:
                        oval = self.dice.create_oval(105,35,120,50, fill="black")
                        oval = self.dice.create_oval(50,105,35,120, fill="black")
                        oval = self.dice.create_oval(105,105,120,120, fill="black")
                        oval = self.dice.create_oval(50,35,35,50, fill="black")
                        oval = self.dice.create_oval(70,70,85,85, fill="black")
                    else: #6
                        oval = self.dice.create_oval(105,25,120,40, fill="black")
                        oval = self.dice.create_oval(50,115,35,130, fill="black")
                        oval = self.dice.create_oval(105,115,120,130, fill="black")
                        oval = self.dice.create_oval(50,25,35,40, fill="black")
                        oval = self.dice.create_oval(50,70,35,85, fill="black")
                        oval = self.dice.create_oval(105,70,120,85, fill="black")
                    
                    #set internal variable to global variable value
                    num = self.num
                    dice_force = False
                    dice_allowed = False
        
        #create dice button and bind function to it
        self.diceButton = Button(self.frame, text = 'würfeln', width = 5)
        self.diceButton.pack(side = "bottom")
        self.diceButton.bind("<Button-1>", roll_dice)

#set Server IP and Port
HOST = "127.0.0.1"
PORT = 61111
#Start connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#Send Codeword to server that new player has joined
data = "NEW"
s.sendall(pickle.dumps(data))

root_window = Tk()
app = canvas(root_window)
app.mainloop()
