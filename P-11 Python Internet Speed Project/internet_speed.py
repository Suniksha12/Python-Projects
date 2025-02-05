from tkinter import *
import speedtest

sp = Tk()
#adding features
sp.title(" Internet Speed Test ")
sp.geometry("500x700")
sp.config(bg="Blue")

lab = Label(sp,text = "Internet Speed Test", font=("Time New Roman",30,"bold"),bg="Blue",fg="white")
lab.place(x=60,y=40, height=50,width=380)

lab = Label(sp,text = "Download Speed", font=("Time New Roman",30,"bold"))
lab.place(x=60,y=130, height=50,width=380)

lab = Label(sp,text = "00", font=("Time New Roman",30,"bold"))
lab.place(x=60,y=200, height=50,width=380)

lab = Label(sp,text = "Uplaod Speed", font=("Time New Roman",30,"bold"))
lab.place(x=60,y=290, height=50,width=380)

lab = Label(sp,text = "00", font=("Time New Roman",30,"bold"))
lab.place(x=60,y=360, height=50,width=380)

#button
button = Button(sp,text="Check Speed", font=("Time New Roman",30,"bold"),relief=RAISED, bg="Red")
button.place(x=60,y=460, height=50,width=380)

sp.mainloop()