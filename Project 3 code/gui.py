#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
def setpos1():
    turtle.setx(x)
    turtle.sety(y)
def setpos2():
    turtle.setx(x)
    turtle.sety(y)
def setpos3():
    turtle.setx(x)
    turtle.sety(y)
def setpos4():
    turtle.setx(x)
    turtle.sety(y)

def retrieve_input():
    input = self.entry.get("1.0",END)
    
    
class simpleapp_tk(Tkinter.Tk):
    amount = 0
    
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def set(self, field):
        entry = self.entry.get()

        if field == "amount":
            self.amount = entry

        print(self.amount)

    def initialize(self):
        self.grid()

        self.button = Tkinter.Button(self, text="Ammount of treasures", command=lambda: self.set("amount"))
        self.button.grid(column=1,row=0,sticky='EW')

        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='EW')

        self.button = Tkinter.Button(self, text="set Position 1", command=setpos1)
        self.button.grid(column=1,row=3,sticky='EW')

        self.button = Tkinter.Button(self, text="set Position 2", command=setpos2)
        self.button.grid(column=1,row=2,sticky='EW')

        self.button = Tkinter.Button(self, text="set Position 3", command=setpos3)
        self.button.grid(column=0,row=3,sticky='EW')

        self.button = Tkinter.Button(self, text="set Position  4", command=setpos4)
        self.button.grid(column=0,row=2,sticky='EW')
      

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.mainloop()
