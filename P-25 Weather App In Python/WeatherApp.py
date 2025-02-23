from tkinter import *

win = Tk()
win.title("Whoosh Tech")

#background color change
win.config(bg="blue")

#geometry and dimension fix
win.geometry("500x500")

#adding the label
name_label = Label(win,text="Whoosh Weather App",
                   font=("Time New Roman",30,"bold"))

name_label.place(x=25,y=50,height=50,width=450)

win.mainloop()