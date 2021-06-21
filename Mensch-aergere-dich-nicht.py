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
        if(event.widget["background"] == "white"):
            print("works")

    def create_board(self):
        self.main_board = Canvas(self,width=800, height=700, bg = "#F5F6CE")
        self.main_board.pack()

        for i in range(0,3,1):
            self.felder.append(self.main_board.create_oval(350+(50*i),75,385+(50*i),110,fill="white"))
            self.felder.append(self.main_board.create_oval(350+(50*i),610,385+(50*i),575,fill="white"))

        for i in range(0,4,1):
            button= self.main_board.create_oval(350,160+(i*50),385,125+(i*50),fill="white", tags="playbutton")
            button= self.main_board.create_oval(350,410+(i*50),385,375+(i*50),fill="white", tags="playbutton")
            button= self.main_board.create_oval(450,160+(i*50),485,125+(i*50),fill="white", tags="playbutton")
            button= self.main_board.create_oval(450,410+(i*50),485,375+(i*50),fill="white", tags="playbutton")
            button= self.main_board.create_oval(300-(i*50),310,335-(i*50),275,fill="white", tags="playbutton")
            button= self.main_board.create_oval(500+(i*50),310,535+(i*50),275,fill="white", tags="playbutton")
            button= self.main_board.create_oval(300-(i*50),410,335-(i*50),375,fill="white", tags="playbutton")
            button= self.main_board.create_oval(500+(i*50),410,535+(i*50),375,fill="white", tags="playbutton")
            
            button= self.main_board.create_oval(400,410+(i*50),435,375+(i*50),fill="red", tags="playbutton")
            button= self.main_board.create_oval(400,160+(i*50),435,125+(i*50),fill="blue", tags="playbutton")
            button= self.main_board.create_oval(200+(i*50),360,235+(i*50),325,fill="green", tags="playbutton")
            button= self.main_board.create_oval(450+(i*50),360,485+(i*50),325,fill="yellow", tags="playbutton")
            
        button=self.main_board.create_oval(150,360,185,325,fill="white", tags="playbutton")
        button= self.main_board.create_oval(650,360,685,325,fill="white", tags="playbutton")
        self.main_board.tag_bind("playbutton", "<Button-1>", self.clicked)

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
