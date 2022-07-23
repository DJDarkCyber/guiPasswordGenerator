#!/usr/bin/env python

from tkinter import * 		# Importing tkinter for gui display
import random				# Importing random to generate random random password

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "@#$^&*!+-"


class passwordGenerator:
    def __init__(self):
        print("Welcome To the Password Generator")
        self.randomPassword = ""
        self.rootDisplay = Tk()
        self.rootDisplay.geometry("400x100")
        self.rootDisplay.config(background="black")
        self.guiApplication()
        
    def randomPassGenerator(self):
        passLen = 18
        for i in range(0, passLen):
            isLetNumSym = random.randint(1, 3)
            if isLetNumSym == 1:
                randLet = letters[random.randint(0, len(letters) - 1)]
                toup = random.randint(0, 1)
                if toup == 1:
                    randLet = randLet.upper()
                self.randomPassword += randLet
            elif isLetNumSym == 2:
                randNum = numbers[random.randint(0, len(numbers) - 1)]
                self.randomPassword += randNum
            elif isLetNumSym == 3:
                randSym = symbols[random.randint(0, len(symbols) - 1)]
                self.randomPassword += randSym
        return self.randomPassword
    
    def copyClipBoard(self):
        self.rootDisplay.clipboard_clear()
        self.rootDisplay.clipboard_append(self.generatedPassword)
        self.copyBtn.destroy()
        copied = Label(self.rootDisplay, text="Copied to clip board")
        copied.config(border=50, foreground='cyan', background="black")
        copied.pack()
    
    def passWordGen(self):
        self.generatedPassword = self.randomPassGenerator()
        self.genBtn.destroy()
        self.passDisp = Label(self.rootDisplay, text=self.generatedPassword)
        self.passDisp.config(foreground="red", background="black")
        self.passDisp.pack()
        self.copyBtn = Button(self.rootDisplay, text="Copy", command=self.copyClipBoard)
        self.copyBtn.config(foreground="cyan", background="aquamarine2", highlightcolor="red", activebackground="blue", activeforeground="aquamarine2")
        self.copyBtn.pack()
    
    def guiApplication(self):
        
        self.genBtn = Button(self.rootDisplay, text="Generate", command=self.passWordGen)
        self.genBtn.config(foreground="cyan", background="aquamarine2", highlightcolor="red", activebackground="blue", activeforeground="aquamarine2")
        self.genBtn.pack()
        self.rootDisplay.mainloop()

passwordGenerator()
