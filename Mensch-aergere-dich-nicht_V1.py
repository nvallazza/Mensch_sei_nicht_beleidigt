from tkinter import *
import random

class canvas(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.felder = [0]*56
        self.master = master
        master.title("Mensch ärgere dich nicht!")
        self.pack()
        self.create_board()
        #self.create_dice(dice_window)

    def create_board(self):
        self.main_board = Canvas(self,width=800, height=700, bg = "#F5F6CE")
        self.main_board.pack()
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
dice_window = Tk()
dice_window.title = "Würfel"
app = canvas(root_window)
app.mainloop()
