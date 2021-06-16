from tkinter import *
import random

class canvas(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.felder = [0]*56
        self.master = master
        self.new_window()
        master.title("Mensch ärgere dich nicht!")
        self.pack()
        self.create_board()
        #self.create_dice(dice_window)
    
    def new_window(self):
            self.newWindow = Toplevel(self.master)
            self.app = Demo2(self.newWindow)

    def create_board(self):
        self.main_board = Canvas(self,width=800, height=700, bg = "#F5F6CE")
        self.main_board.pack()
        #oval = self.main_board.create_polygon(20,20,780,20,780,680,20,680, outline="red", fill="", width=3)
        a=0
        for i in range(0,3,1):
            self.felder[a] = self.main_board.create_oval(350+(50*i),75,385+(50*i),110,fill="white")
            self.felder[a+3] = self.main_board.create_oval(350+(50*i),610,385+(50*i),575,fill="white")
            a+=1
        a=6
        for i in range(0,4,1):
            self.felder[a] = self.main_board.create_oval(350,160+(i*50),385,125+(i*50),fill="white")
            self.felder[a+4] = self.main_board.create_oval(350,410+(i*50),385,375+(i*50),fill="white")
            self.felder[a+8] = self.main_board.create_oval(450,160+(i*50),485,125+(i*50),fill="white")
            self.felder[a+12] = self.main_board.create_oval(450,410+(i*50),485,375+(i*50),fill="white")
            self.felder[a+16] = self.main_board.create_oval(300-(i*50),310,335-(i*50),275,fill="white")
            self.felder[a+20] = self.main_board.create_oval(500+(i*50),310,535+(i*50),275,fill="white")
            self.felder[a+24] = self.main_board.create_oval(300-(i*50),410,335-(i*50),375,fill="white")#300,360
            self.felder[a+28] = self.main_board.create_oval(500+(i*50),410,535+(i*50),375,fill="white")
            
            self.felder[a+32] = self.main_board.create_oval(400,410+(i*50),435,375+(i*50),fill="red")
            self.felder[a+36] = self.main_board.create_oval(400,160+(i*50),435,125+(i*50),fill="blue")
            self.felder[a+40] = self.main_board.create_oval(200+(i*50),360,235+(i*50),325,fill="green")
            self.felder[a+44] = self.main_board.create_oval(450+(i*50),360,485+(i*50),325,fill="yellow")
            a+=1
            
        self.felder[54] = self.main_board.create_oval(150,360,185,325,fill="white")
        self.felder[55] = self.main_board.create_oval(650,360,685,325,fill="white")

class Demo2:
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
        
    #def create_dice(self,dice_window):
     #   dice_window.title = "Würfel"
      #  self.pack()
            #self.dice = Button(self)
            #self.dice["text"]="Würfeln"
            #self.dice["font"]= tkFont.Font(size=16,family="Calibri")
            #self.dice.bind("<ButtonPress-1>", self.create_pic)
            #self.dice.pack()
            
       #     break
        
root_window = Tk()
app = canvas(root_window)
app.mainloop()
