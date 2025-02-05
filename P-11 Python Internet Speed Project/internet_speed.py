from tkinter import *
import speedtest

sp = Tk()
#adding features
sp.title(" Internet Speed Test ")
sp.geometry("500x500")
sp.config(bg="Blue")

lab = Label(sp,text = "Internet Speed Test", font=("Time New Roman",30,"bold"),bg="Blue",fg="white")
lab.place(x=60,y=40)

lab = Label(sp,text = "Download Speed", font=("Time New Roman",30,"bold"),bg="Blue",fg="white")
lab.place(x=60,y=40)

lab = Label(sp,text = "00", font=("Time New Roman",30,"bold"),bg="Blue",fg="white")
lab.place(x=60,y=40)

lab = Label(sp,text = "Uplaod Speed", font=("Time New Roman",30,"bold"),bg="Blue",fg="white")
lab.place(x=60,y=40)

lab = Label(sp,text = "00", font=("Time New Roman",30,"bold"),bg="Blue",fg="white")
lab.place(x=60,y=40)

sp.mainloop()