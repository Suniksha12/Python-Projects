from tkinter import *
#now we ill use combo box
from tkinter import ttk
#we need data for which we will bring the api
import requests

#creating a function
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c13caae56a50320d26f03c71890014d6").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Whoosh Tech")

#background color change
win.config(bg="blue")

#geometry and dimension fix
win.geometry("500x570")

#adding the label
name_label = Label(win,text="Whoosh Weather App",
                   font=("Time New Roman",30,"bold"))

name_label.place(x=25,y=50,height=50,width=450)

#using the combo box
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Whoosh Weather App",values=list_name,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=50, width=450)

w_label = Label(win,text="Weather Climate",
                   font=("Time New Roman",20))

w_label.place(x=25,y=260,height=50,width=210)

#substitute label
w_label1 = Label(win,text="",
                   font=("Time New Roman",20))

w_label1.place(x=250,y=260,height=50,width=210)

wb_label = Label(win,text="Weather Description",
                   font=("Time New Roman",17))

wb_label.place(x=25,y=330,height=50,width=210)

#substitute label
wb_label1 = Label(win,text="",
                   font=("Time New Roman",17))

wb_label1.place(x=250,y=330,height=50,width=210)


temp_label = Label(win,text="Temperature",
                   font=("Time New Roman",20))

temp_label.place(x=25,y=400,height=50,width=210)

#substitute label
temp_label1 = Label(win,text="",
                   font=("Time New Roman",20))

temp_label1.place(x=250,y=400,height=50,width=210)

per_label = Label(win,text="Pressure",
                   font=("Time New Roman",20))

per_label.place(x=25,y=470,height=50,width=210)

#substitute label
per_label1 = Label(win,text="",
                   font=("Time New Roman",20))

per_label1.place(x=250,y=470,height=50,width=210)

#building a button
done_button = Button(win,text="Done",
                     font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()