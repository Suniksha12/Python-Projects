from tkinter import *
#now we ill use combo box
from tkinter import ttk

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

#using the combo box
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Whoosh Weather App",values=list_name,
                   font=("Time New Roman",20,"bold"))

com.place(x=25,y=120,height=50, width=450)

win.mainloop()