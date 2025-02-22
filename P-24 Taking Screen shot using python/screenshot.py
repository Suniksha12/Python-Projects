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

#building a function
def take_ss():
    #how to get the data into entry box
    add_data = entry.get()
    path = add_data+"\\test.png"
    print(path)
    # ss = pyautogui.screenshot()
    # ss.save("test1.png")

win = Tk()
win.title("Win ScreenShot")
win.geometry("700x400")
win.config(bg="yellow")
win.resizable(False, False)

entry = Entry(win, font=('Time New Roman',30))
entry.place(x=20, height=70, width=660, y=50)

button = Button(win,text="Done", font=('Time New Roman',50),command=take_ss)
button.place(x=250,y=140,height=100,width=200)

win.mainloop()