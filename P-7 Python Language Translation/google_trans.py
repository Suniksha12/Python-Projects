from tkinter import *
from tkinter import ttk

#now we wil make the translator work
from googletrans import Translator, LANGUAGES

#defining a function for conversion
def change(text="type",src="English",dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans=Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1

def data():
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

list_text = list(LANGUAGES.values())

comb1_sor = ttk.Combobox(frame,value=list_text)
comb1_sor.place(x=10,y=300,height=40,width=150)
comb1_sor.set("English")

#we will make the button for language change
button_change = Button(frame,text="Translate",relief=RAISED)
button_change.place(x=170,y=300,height=40,width=150)

#destination combo box
comb1_dest = ttk.Combobox(frame,value=list_text)
comb1_dest.place(x=330,y=300,height=40,width=150)
comb1_dest.set("English")

#making destination text box
lab_txt = Label(root,text="Destination Text",font=("Time New Roman",20,"bold"),fg="Black",bg="Red")
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(frame,font=("Time New Roman",40,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()

