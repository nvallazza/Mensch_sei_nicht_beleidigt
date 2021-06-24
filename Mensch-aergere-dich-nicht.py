from tkinter import *
from tkinter import messagebox
import random

global num
num = 0

global dice_allowed
dice_allowed = True

global dice_force
dice_force = True

global count
count = True

class canvas(Frame):
    def __init__(self, master=None):
        global count
        super().__init__(master)
        self.coords = []
        self.master = master
        self.newWindow = Toplevel(self.master)
        self.newWindow.after(1, lambda: self.newWindow.focus_force())
        Dice(self.newWindow)
        master.title("Mensch ärgere dich nicht!")
        self.pack()
        self.create_board()
    
    def new_window(self, event):
        global dice_allowed, dice_force, count
        self.caller = event.widget.find_withtag("current")[0]
        if dice_force == True:
            Dice(self.newWindow)
            
        if dice_allowed==False:
            y=list(self.coords[self.caller-1])
            if y[4]=="white":
                return
            self.clicked()
    
    def clicked(self):
        global num,dice_allowed
        for j in range (0,5,1):
            for i in range (j+1,7,1):
                if ( self.caller == (40-j) and num == i):
                    y=list(self.coords[1+(i-j)])
                    y[4]="red"
                    self.coords[1+(i-j)]=y
                    self.main_board.itemconfigure((i-j),fill="red")
                    print("you clicked:"+str(self.caller))
                    print(self.coords[0])
                    dice_allowed = True
                    self.main_board.itemconfigure(self.caller, fill = "white")
                    return
                    
        y=list(self.coords[self.caller+num-1])
        y[4]="red"
        self.coords[self.caller+num-1]=y
        y=list(self.coords[self.caller-1])
        if y[0] == 450 and y[1] == 75:
            self.main_board.itemconfigure(self.caller, fill = "#819FF7")
        elif y[0] == 650 and y[1] == 410:
            self.main_board.itemconfigure(self.caller, fill = "#F3F781")
        elif y[0] == 350 and y[1] == 610:
            self.main_board.itemconfigure(self.caller, fill = "#F78181")
        elif y[0] == 150 and y[1] == 310:
            self.main_board.itemconfigure(self.caller, fill = "#81F781")
        else:
            self.main_board.itemconfigure(self.caller, fill = "white")
            
        self.main_board.itemconfigure(self.caller+num,fill="red")
        print("you clicked:"+str(self.caller))
        dice_allowed = True

    def create_board(self):
        global num
        x0 = 0
        x1 = 0
        y0 = 0
        y1 = 0
        color = ""
        self.main_board = Canvas(self,width=800, height=700, bg = "#F5F6CE")
        self.main_board.pack()
        
        for i in range(0,2,1):
            self.coords.append((350+(50*i),75,385+(50*i),110,"#FFFFFF"))
        self.coords.append((450,75,485,110,"#819FF7"))
        for i in range(0,4,1):
            self.coords.append((450,160+((i)*50),485,125+((i)*50),"white"))
        for i in range(0,4,1):
            self.coords.append((500+((i)*50),310,535+((i)*50),275,"white"))
        self.coords.append((650,360,685,325,"white"))
        self.coords.append((650,410,685,375,"#F3F781"))
        for i in range(1,4,1):
            self.coords.append((650-((i)*50),410,685-((i)*50),375,"white"))
        for i in range(0,4,1):
            self.coords.append((450,410+((i)*50),485,375+((i)*50),"white"))
        for i in range(0,2,1):
            self.coords.append((450-(50*i),610,485-(50*i),575,"white"))
        self.coords.append((350,610,385,575,"#F78181"))
        for i in range(0,4,1):
            self.coords.append((350,560-(i*50),385,525-(i*50),"white"))
        for i in range(0,4,1):
            self.coords.append((300-((i)*50),410,335-((i)*50),375,"white"))
        self.coords.append((150,360,185,325,"white"))
        self.coords.append((150,310,185,275,"#81F781"))
        for i in range(1,4,1):
            self.coords.append((150+((i)*50),310,185+((i)*50),275,"white"))
        for i in range(0,4,1):
            self.coords.append((350,310-(i*50),385,275-(i*50),"white"))
            
        for i in range(0,4,1):
            self.coords.append((400,410+((i)*50),435,375+((i)*50),"#F78181"))
        for i in range(0,4,1):
            self.coords.append((400,160+((i)*50),435,125+((i)*50),"#819FF7"))
        for i in range(0,4,1):
            self.coords.append((200+((i)*50),360,235+((i)*50),325,"#81F781"))
        for i in range(0,4,1):
            self.coords.append((450+((i)*50),360,485+((i)*50),325,"#F3F781"))
        
        for i in range (1,57,1):
            myTag = "{}".format(i)
            x0 = self.coords[i-1][0]
            y0 = self.coords[i-1][1]
            x1 = self.coords[i-1][2]
            y1 = self.coords[i-1][3]
            color = self.coords[i-1][4]
            field= self.main_board.create_oval(x0,y0,x1,y1,fill=color,tags=myTag)
            self.main_board.tag_bind(myTag, "<Button-1>", self.new_window)
            
        self.main_board.create_oval(650,75,685,110,fill="#819FF7")
        self.main_board.create_oval(600,75,635,110,fill="#819FF7")
        self.main_board.create_oval(650,125,685,160,fill="#819FF7")
        self.main_board.create_oval(600,125,635,160,fill="#819FF7")
        
        self.main_board.create_oval(150,75,185,110,fill="#81F781")
        self.main_board.create_oval(200,75,235,110,fill="#81F781")
        self.main_board.create_oval(150,125,185,160,fill="#81F781")
        self.main_board.create_oval(200,125,235,160,fill="#81F781")
        
        self.main_board.create_oval(150,610,185,575,fill="#F78181")
        self.main_board.create_oval(200,610,235,575,fill="#F78181")
        self.main_board.create_oval(150,560,185,525,fill="#F78181")
        self.main_board.create_oval(200,560,235,525,fill="#F78181")
        
        self.main_board.create_oval(650,610,685,575,fill="#F3F781")
        self.main_board.create_oval(650,560,685,525,fill="#F3F781")
        self.main_board.create_oval(600,610,635,575,fill="#F3F781")
        self.main_board.create_oval(600,560,635,525,fill="#F3F781")
            
class Dice:
    def __init__(self, master):
        self.master = master
        master.title("Würfel")
        master.geometry("200x200")
        self.play()
        
    def play(self):
        self.frame = Frame(self.master)
        self.frame.pack()
        self.dice = Canvas(self.frame ,width=150, height=150, bg = "#F5F6CE")
        self.dice.pack()
        self.dice_allowed = True
        def roll_dice(event):
            global num, dice_allowed, dice_force, count
            while (dice_allowed == True):
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
                    count = False
                    oval = self.dice.create_oval(105,25,120,40, fill="black")
                    oval = self.dice.create_oval(50,115,35,130, fill="black")
                    oval = self.dice.create_oval(105,115,120,130, fill="black")
                    oval = self.dice.create_oval(50,25,35,40, fill="black")
                    oval = self.dice.create_oval(50,70,35,85, fill="black")
                    oval = self.dice.create_oval(105,70,120,85, fill="black")
                
                num = self.num
                dice_force = False
                print(num)
                dice_allowed = False
        
        self.diceButton = Button(self.frame, text = 'würfeln', width = 5)
        self.diceButton.pack(side = "bottom")
        self.diceButton.bind("<Button-1>", roll_dice)
        
root_window = Tk()
app = canvas(root_window)
app.mainloop()
