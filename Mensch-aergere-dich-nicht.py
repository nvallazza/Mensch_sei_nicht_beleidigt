from tkinter import *
import random

class canvas(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.felder = []
        self.master = master
        self.new_window()
        master.title("Mensch ärgere dich nicht!")
        self.pack()
        self.create_board()
    
    def new_window(self):
            self.newWindow = Toplevel(self.master)
            self.app = Dice(self.newWindow)
    
    def clicked(self, event):
        caller = event.widget.find_withtag("current")[0]
        self.main_board.itemconfigure(caller,fill="red")
        print("you clicked:"+str(caller))

    def create_board(self):
        x0 = 0
        x1 = 0
        y0 = 0
        y1 = 0
        color = ""
        self.coords = []
        self.main_board = Canvas(self,width=800, height=700, bg = "#F5F6CE")
        self.main_board.pack()
        
        for i in range(0,3,1):
            self.coords.append((350+(50*i),75,385+(50*i),110,"white"))
        for i in range(0,3,1):
            self.coords.append((350+(50*i),610,385+(50*i),575,"white"))
        for i in range(0,4,1):
            self.coords.append((350,160+(i*50),385,125+(i*50),"white"))
        for i in range(0,4,1):
            self.coords.append((350,410+(i*50),385,375+(i*50),"white"))
        for i in range(0,4,1):
            self.coords.append((450,160+((i)*50),485,125+((i)*50),"white"))
        for i in range(0,4,1):
            self.coords.append((450,410+((i)*50),485,375+((i)*50),"white"))
        for i in range(0,4,1):
            self.coords.append((300-((i)*50),310,335-((i)*50),275,"white"))
        for i in range(0,4,1):
            self.coords.append((500+((i)*50),310,535+((i)*50),275,"white"))
        for i in range(0,4,1):
            self.coords.append((300-((i)*50),410,335-((i)*50),375,"white"))
        for i in range(0,4,1):
            self.coords.append((500+((i)*50),410,535+((i)*50),375,"white"))
        for i in range(0,4,1):
            self.coords.append((400,410+((i)*50),435,375+((i)*50),"#F78181"))
        for i in range(0,4,1):
            self.coords.append((400,160+((i)*50),435,125+((i)*50),"#819FF7"))
        for i in range(0,4,1):
            self.coords.append((200+((i)*50),360,235+((i)*50),325,"#81F781"))
        for i in range(0,4,1):
            self.coords.append((450+((i)*50),360,485+((i)*50),325,"#F3F781"))
        self.coords.append((150,360,185,325,"white"))
        self.coords.append((650,360,685,325,"white"))
        
        for i in range (1,57,1):
            myTag = "{}".format(i)
            x0 = self.coords[i-1][0]
            y0 = self.coords[i-1][1]
            x1 = self.coords[i-1][2]
            y1 = self.coords[i-1][3]
            color = self.coords[i-1][4]
            button= self.main_board.create_oval(x0,y0,x1,y1,fill=color,tags=myTag)
            self.main_board.tag_bind(myTag, "<Button-1>", self.clicked)

class Dice:
    def __init__(self, master):
        self.master = master
        master.title("Dice")
        master.geometry("200x200")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.dice = Canvas(self.frame ,width=150, height=150, bg = "#F5F6CE")
        self.dice.pack()
        self.diceButton = Button(self.frame, text = 'Dice', width = 5, command = self.roll_dice)
        self.diceButton.pack(side = "bottom")

    def roll_dice(self):
        self.dice.delete("all")
        self.num = random.randint(1,6)
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
        else:
            oval = self.dice.create_oval(105,25,120,40, fill="black")
            oval = self.dice.create_oval(50,115,35,130, fill="black")
            oval = self.dice.create_oval(105,115,120,130, fill="black")
            oval = self.dice.create_oval(50,25,35,40, fill="black")
            oval = self.dice.create_oval(50,70,35,85, fill="black")
            oval = self.dice.create_oval(105,70,120,85, fill="black")
        
root_window = Tk()
app = canvas(root_window)
app.mainloop()
