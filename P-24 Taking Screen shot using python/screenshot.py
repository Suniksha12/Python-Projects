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
import os
from tkinter import *

#building a function
# Function to take a screenshot and save it to the user-defined path
def take_ss():
    add_data = entry.get().strip()  # Get the path from entry box & remove spaces
    
    if not add_data:  # Check if input is empty
        label_status.config(text="Error: Please enter a valid path", fg="red")
        return
    
    # Ensure directory exists
    if not os.path.exists(add_data):
        os.makedirs(add_data)  # Create the directory if it doesn't exist

    path = os.path.join(add_data, "test.png")  # Construct file path
    try:
        ss = pyautogui.screenshot()
        ss.save(path)
        label_status.config(text=f"Screenshot saved at:\n{path}", fg="green")
    except Exception as e:
        label_status.config(text=f"Error: {str(e)}", fg="red")

win = Tk()
win.title("Win ScreenShot")
win.geometry("700x400")
win.config(bg="yellow")
win.resizable(False, False)

entry = Entry(win, font=('Time New Roman',30))
entry.place(x=20, height=70, width=660, y=50)

button = Button(win,text="Done", font=('Time New Roman',50),command=take_ss)
button.place(x=250,y=140,height=100,width=200)

# Status label to show messages
label_status = Label(win, text="", font=('Times New Roman', 14), bg="yellow")
label_status.place(x=20, y=220, width=660)

win.mainloop()