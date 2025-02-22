# import pyautogui


# ss = pyautogui.screenshot()

# #save the file
# ss.save("test1.png")

#in ths we will make a desktop application for this once you have run your program
#ultimately you can find that your screenshot is being saved in the same directory 
#where you have saved your program file

#now in order to make an application we will require a module Tkinter 
#open your command prompt and in it just put the command
#syntax : pip install tkintertable

import pyautogui
from tkinter import *

win = Tk()
win.title("Win ScreenShot")
win.geometry("400x300")
win.config(bg="yellow")
win.resizable(False, False)

button = Button(win,text="Done", font=('Time New Roman',50,"bold"))
button.place(x=100,y=100,height=100,width=200)

win.mainloop()