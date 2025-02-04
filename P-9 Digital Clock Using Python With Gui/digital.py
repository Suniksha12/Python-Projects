from tkinter import *

clock = Tk()

#chanege the title
clock.title('       ****Digital Clock****       ')
clock.geometry('1000x500')
clock.config(bg='yellow')

#calling the label function
lab_hr = Label(clock,text="00",font=('Time New Roman',60,"bold"),
               bg='red',fg="white")
lab_hr.place()

clock.mainloop()
