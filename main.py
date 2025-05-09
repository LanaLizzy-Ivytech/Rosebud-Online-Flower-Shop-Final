'''
Author: Lana Hendrickson
Date: 5/3/2025
Assigment: Final Project
Create a program that can accept a user's input on flower arrangements and give back their total
'''

#import
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

#varables
TULIP_COST = 15.00
DAISY_COST = 20.00
PURPLE_COST = 3.00
WHITE_COST = 5.00
TAX_RATE = 0.10
flowerCheck = 0
colorCheck = 0


#The main window
class windowHome(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, title = "Rosebud Online Flower Shop")
        self.addLabel(text = "Rosebud Online Flower Shop", row = 0, column = 1, sticky = "N")
        #Order flower type
        self.addLabel(text = "Current bouquets available to order:", row = 3, column = 1, sticky = "N")
        self.tulipBtn = self.addButton(text = "Tulip: $15.00", row = 4, column = 0, command = self.tulipBtn)
        self.daisyBtn = self.addButton(text = "Daisy: $20.00", row = 4, column = 2, command = self.daisyBtn)
        #Order color type
        self.addLabel(text = "Current colors available to order:", row = 6, column = 1, sticky = "N")
        self.purpleBtn = self.addButton(text = "Purple: $3.00", row = 7, column = 0, command = self.purpleBtn)
        self.whiteBtn = self.addButton(text = "White: $5.00", row = 7, column = 2, command = self.whiteBtn)
        #Movement/Control buttons
        self.resetBtn = self.addButton(text = "Reset Order", row = 8, column = 1, command = self.reset)
        self.orderBtn = self.addButton(text = "Confirm Order", row = 9, column = 1, command = self.order)
        self.exitBtn = self.addButton(text = "Exit Program", row = 10, column = 1, command = self.exit)

    #The tulip button
    def tulipBtn(self):
        self.daisyBtn["state"] = "disable"
        global flowerCheck
        flowerCheck = 1

    #The daisy button
    def daisyBtn(self):
        self.tulipBtn["state"] = "disable"
        global flowerCheck
        flowerCheck = 2

    #The purple button
    def purpleBtn(self):
        self.whiteBtn["state"] = "disable"
        global colorCheck
        colorCheck = 1

    #The white button
    def whiteBtn(self):
        self.purpleBtn["state"] = "disable"
        global colorCheck
        colorCheck = 2

    #Reset all the option buttons
    def reset(self):
        self.daisyBtn["state"] = "normal"
        self.tulipBtn["state"] = "normal"
        self.purpleBtn["state"] = "normal"
        self.whiteBtn["state"] = "normal"
        global flowerCheck
        global colorCheck
        colorCheck = 0
        flowerCheck = 0

    #Opens the order window
    def order(self):
        self.destroy()
        windowOrder().mainloop()

    #Opens the exit window
    def exit(self):
        self.destroy()
        windowExit().mainloop()

#Open a window telling what flowers total is
class windowOrder(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Rosebud Online Flower Shop")
        self.addLabel(text = "Order Page", row = 0, column = 1, sticky = "N")
        #checking that button were pressed
        if colorCheck == 0 or flowerCheck == 0:
            self.addLabel(text = "One or more button were not pressed please go back to place a order", row = 2, column = 1, sticky = "N")
            self.addLabel(text = "No order placed", row = 3, column = 1, sticky = "N")
        #checking that tulip and purple was pressed
        elif colorCheck == 1 and flowerCheck == 1:
            total = (TULIP_COST + PURPLE_COST) * TAX_RATE
            self.addLabel(text = "Your flowers were tulip with the color purple totaling at", row = 2, column = 1, sticky = "N")
            self.addLabel(text = total, row = 3, column = 1, sticky = "N")
        #checking that tulip and white was pressed
        elif colorCheck == 2 and flowerCheck == 1:
            total = (TULIP_COST + WHITE_COST) * TAX_RATE
            self.addLabel(text = "Your flowers were tulip with the color white totaling at", row = 2, column = 1, sticky = "N")
            self.addLabel(text = total, row = 3, column = 1, sticky = "N")
        #checking that daisy and purple was pressed
        elif colorCheck == 1 and flowerCheck == 2:
            total = (DAISY_COST + PURPLE_COST) * TAX_RATE
            self.addLabel(text = "Your flowers were daisy with the color purple totaling at", row = 2, column = 1, sticky = "N")
            self.addLabel(text = total, row = 3, column = 1, sticky = "N")
        #checking that daisy and white was pressed
        elif colorCheck == 2 and flowerCheck == 2:
            total = (DAISY_COST + WHITE_COST) * TAX_RATE
            self.addLabel(text = "Your flowers were daisy with the color white totaling at", row = 2, column = 1, sticky = "N")
            self.addLabel(text = total, row = 3, column = 1, sticky = "N")
            
        self.homeBtn = self.addButton(text = "Home Window", row = 4, column = 1, command = self.home)
        self.exitBtn = self.addButton(text = "Exit Program", row = 5, column = 1, command = self.exit)

    #Open the home window
    def home(self):
        self.destroy()
        windowHome().mainloop()
        global flowerCheck
        global colorCheck
        colorCheck = 0
        flowerCheck = 0
        
    #Opens the exit window
    def exit(self):
        self.destroy()
        windowExit().mainloop()
            
    

#Open a window to instruct the user to close the window
class windowExit(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, title = "Rosebud Online Flower Shop")
        self.addLabel(text = "Press the 'x' in the top corner to close", row = 0, column = 1, sticky = "N")

        

def main():
    windowHome().mainloop()
        
        
    
if __name__ == "__main__":
    main()