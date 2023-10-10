from tkinter.ttk import *
from tkinter import*
from pygame import mixer
from threading import Thread
from datetime import datetime
from time import sleep

root= Tk()
root.title("Alarm Clock")
root.geometry("400x200")

#Main Frame
frame_body= Frame(root,height=200,width=400,bg="sky blue")
frame_body.pack()

#Labels in the frame
name= Label(frame_body,text="ALARM CLOCK",height=1,font="comicsanms 20 bold",bg="sky blue")
name.place(x=10,y=10)

hours=Label(frame_body,text="Hours",height=1,font="comicsanms 14 bold",bg="sky blue")
hours.place(x=20,y=60)
com_hr=Combobox(frame_body,width=4,font="arial 12")
com_hr["values"]=("00","01","02","03","04","05","06","07","08","09","10","11","12")
com_hr.set("00")
com_hr.place(x=23,y=100)

minute=Label(frame_body,text="Minutes",height=1,font="comicsanms 14 bold",bg="sky blue")
minute.place(x=100,y=60)
com_min=Combobox(frame_body,width=4,font="arial 12")
com_min["values"]=()
lst=list(com_min["values"])
for i in range(1,61):
    lst.append(i)
    i+=1
    res=tuple(lst)
    com_min["values"]=(res)
com_min.set("00")
com_min.place(x=110,y=100)

second=Label(frame_body,text="Seconds",height=1,font="comicsanms 14 bold",bg="sky blue")
second.place(x=200,y=60)
com_sec=Combobox(frame_body,width=4,font="arial 12")
com_sec["values"]=()
lst=list(com_sec["values"])
for i in range(1,61):
    lst.append(i)
    i+=1
    res=tuple(lst)
    com_sec["values"]=(res)
com_sec.set("00")
com_sec.place(x=210,y=100)

period=Label(frame_body,text="Period",height=1,font="comicsanms 14 bold",bg="sky blue")
period.place(x=300,y=60)
com_per=Combobox(frame_body,width=4,font="arial 12")
com_per["values"]=("AM","PM")
com_per.set("AM")
com_per.place(x=305,y=100)

def activate_alarm():
    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print('Deactivated alarm: ', selected.get())
    mixer.music.stop()

selected = IntVar()

rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value = 1, text = "Activate", bg="white", command=activate_alarm, variable=selected)
rad1.place(x = 90, y=150)

def sound_alarm():
    mixer.music.load('C:/Users/kshitiz/Music/joki.wav')
    mixer.music.play()
    selected.set(0)

    rad2 = Radiobutton(frame_body, font=('arial 10 bold'), value = 2, text = "Deactivate", bg="white", command=deactivate_alarm, variable=selected)
    rad2.place(x = 185, y=150)

def alarm():
    while True:
        control = selected.get()
        print(control)

        alarm_hour=com_hr.get()
        alarm_minute = com_min.get()
        alarm_sec = com_sec.get()
        alarm_period = com_per.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Times up")
                            sound_alarm()
        sleep(1)

mixer.init()

root.mainloop()