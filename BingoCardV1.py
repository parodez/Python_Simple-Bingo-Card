from tkinter import *
import random

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init__window()

    def init__window(self):
        bingo_frame:Frame = Frame(self)
        bingo_frame.grid(row=0,column=0,columnspan=5)
        Label(bingo_frame,
              text='B',
              height=2,
              width=4,
              bg='blue',
              fg='white',
              font='Times 15 bold',
              relief=RAISED).grid(row=0,column=1)
        Label(bingo_frame,text='I',
              height=2,
              width=4,
              bg='blue',
              fg='white',
              font='Times 15 bold',
              relief=RAISED).grid(row=0,column=2)
        Label(bingo_frame,text='N',
              height=2,
              width=4,
              bg='blue',
              fg='white',
              font='Times 15 bold',
              
              relief=RAISED).grid(row=0,column=3)
        Label(bingo_frame,text='G',
              height=2,
              width=4,
              bg='blue',
              fg='white',
              font='Times 15 bold',
              relief=RAISED).grid(row=0,column=4)
        Label(bingo_frame,text='O',
              height=2,
              width=4,
              bg='blue',
              fg='white',
              font='Times 15 bold',
              relief=RAISED).grid(row=0,column=5)
        
        bingoNumbers_frame:Frame = Frame(self)
        bingoNumbers_frame.grid(row=1,column=0,columnspan=5)

        self.generatedNumbers:list[int] = []
        displayString:str = ''
        for c in range(0,5):
            for r in range(0,5):
                if c == 2 and r == 2:
                    displayString = ''
                elif c == 0:
                    displayString = self.GenerateNumber(0,16)
                elif c == 1:
                    displayString = self.GenerateNumber(15,31)
                elif c == 2:
                    displayString = self.GenerateNumber(30,46)
                elif c == 3:
                    displayString = self.GenerateNumber(45,61)
                elif c == 4:
                    displayString = self.GenerateNumber(60,76)
                Label(bingoNumbers_frame,text=displayString,
                        height=2,
                        width=4,
                        bg='white',
                        fg='blue',
                        font='Times 15 bold',
                        relief=RAISED).grid(row=r,column=c)
                
        self.pack()

    def GenerateNumber(self,min,max):
        while True:
            randomNumber = random.randrange(min,max)
            if randomNumber not in self.generatedNumbers:  
                break
        self.generatedNumbers.append(randomNumber)

        return str(randomNumber)

root = Tk()
root.title('Final Exam A')
app = Window(root)
root.mainloop()