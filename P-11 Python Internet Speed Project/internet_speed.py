from tkinter import *
import speedtest
import threading

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps "
    up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps "
    
    # Schedule the update on the main thread
    lab_down.after(0, lambda: lab_down.config(text=down))
    lab_up.after(0, lambda: lab_up.config(text=up))

def start_speed_test():
    thread = threading.Thread(target=speedcheck)
    thread.start()

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="Blue")

lab = Label(sp, text="Internet Speed Test", font=("Time New Roman", 30, "bold"), bg="Blue", fg="yellow")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download Speed", font=("Time New Roman", 30, "bold"))
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Time New Roman", 30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Upload Speed", font=("Time New Roman", 30, "bold"))
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Time New Roman", 30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="Check Speed", font=("Time New Roman", 30, "bold"), relief=RAISED, bg="Red", command=start_speed_test)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
