from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Red')

lab_txt = Label(root,text="Translator",font=("Time New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

#we will make a frame for different slabs
frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="Black",bg="Red")
lab_txt.place(x=100,y=100,height=20,width=300)

#Now we will get two text boxes one for the source and the other for the destination
Sor_txt = Text(frame,font=("Time New Roman",40,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)


root.mainloop()

