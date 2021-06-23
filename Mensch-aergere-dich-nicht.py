from tkinter import *
from tkinter import messagebox
import random
import time

global num
num = 0

class canvas(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.coords = []
        self.master = master
        self.newWindow = Toplevel(self.master)
        self.newWindow.after(1, lambda: self.newWindow.focus_force())
        self.first_throw = Dice(self.newWindow)
        #self.master.wait_window(self.newWindow)
        master.title("Mensch ärgere dich nicht!")
        self.pack()
        self.create_board()
    
    def new_window(self, event):
        #if num == 0:
        #    self.newWindow = Toplevel(self.master)
        self.caller = event.widget.find_withtag("current")[0]
        if self.first_throw==1:
            print("huhu")
        y=list(self.coords[self.caller-1])
        if y[4]=="white":
            messagebox.showerror("Achtung!", "Keine Spielfigur auf diesem Feld!")
            return
        #self.newWindow.destroy()
        self.newWindow = Toplevel(self.master)
        #self.master.wait_window(self.newWindow)
        Dice(self.newWindow)
        self.clicked()
        self.newWindow.destroy()
    
    def clicked(self):
        global num
        y=list(self.coords[self.caller-1])
        y[4]="red"
        self.coords[self.caller-1]=y
        self.caller = self.caller+num
        self.main_board.itemconfigure(self.caller,fill="red")
        print("you clicked:"+str(self.caller))

    def create_board(self):
        global num
        x0 = 0
        x1 = 0
        y0 = 0
        y1 = 0
        color = ""
        self.main_board = Canvas(self,width=800, height=700, bg = "#F5F6CE")
        self.main_board.pack()
        
        for i in range(0,3,1):
            self.coords.append((350+(50*i),75,385+(50*i),110,"white"))
        for i in range(0,4,1):
            self.coords.append((450,160+((i)*50),485,125+((i)*50),"white"))
        for i in range(0,4,1):
            self.coords.append((500+((i)*50),310,535+((i)*50),275,"white"))
        self.coords.append((650,360,685,325,"white"))
        for i in range(0,4,1):
            self.coords.append((650-((i)*50),410,685-((i)*50),375,"white"))
        for i in range(0,4,1):
            self.coords.append((450,410+((i)*50),485,375+((i)*50),"white"))
        for i in range(0,3,1):
            self.coords.append((450-(50*i),610,485-(50*i),575,"white"))
        for i in range(0,4,1):
            self.coords.append((350,560-(i*50),385,525-(i*50),"white"))
        for i in range(0,4,1):
            self.coords.append((300-((i)*50),410,335-((i)*50),375,"white"))
        self.coords.append((150,360,185,325,"white"))
        for i in range(0,4,1):
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
            
    def gameplay(self):
        self.new_window()
            
class Dice:
    def __init__(self, master):
        self.master = master
        master.title("Dice")
        master.geometry("200x200")
        self.play()
        
    def play(self):
        self.frame = Frame(self.master)
        self.frame.pack()
        self.dice = Canvas(self.frame ,width=150, height=150, bg = "#F5F6CE")
        self.dice.pack()
        def roll_dice(event):
            global num
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
            num = self.num
            print(num)
            if num == 6:
                #self.master.destroy()
                return 1
            else:
                #self.master.destroy()
                return 0
        
        self.diceButton = Button(self.frame, text = 'Dice', width = 5)
        self.diceButton.pack(side = "bottom")
        self.diceButton.bind("<Button-1>", roll_dice)
        
root_window = Tk()
app = canvas(root_window)
app.mainloop()
