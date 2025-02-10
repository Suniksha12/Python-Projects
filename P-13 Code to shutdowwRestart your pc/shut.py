from tkinter import *
import os

st = Tk()

#adding external features
st.title("ShutDown App")

st.geometry("500x500")

st.config(bg="Blue")

#we will include four button restart , logoff , and shutdown and restart with time
# we will use button function for this
r_button = Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus")

r_button.place(x=150,y=60,height=50, width=200)

rt_button = Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus")

rt_button.place(x=150,y=170,height=50, width=200)

lg_button = Button(st,text="Log-Out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus")

lg_button.place(x=150,y=270,height=50, width=200)

st_button = Button(st,text="ShutDown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus")

st_button.place(x=150,y=370,height=50, width=200)

st.mainloop()
