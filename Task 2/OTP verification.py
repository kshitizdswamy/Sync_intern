import tkinter.messagebox as tmsg
import math
import random
import smtplib
from tkinter import *

root=Tk()
root.title("OTP Verification")
root.geometry("400x200")

#main frame
frame=Frame(root,height=250,width=400,bg="grey")
frame.pack()

#commands
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP+= digits[math.floor(random.randint(0,9))]
    otp = OTP + " is your OTP.\nDon't share this one time password with anyone."
    msg = otp
def sending():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("interproject777@gmail.com", "ektf azxt mrhc sugd")
    s.sendmail('&&&&&&&&&&&',el2.get(), msg)
    z=tmsg.showinfo("otp sent","Please check given email for otp ")


def verification():
  if el3.get() == OTP:
      a=tmsg.showinfo("Verification Sucess","Yes, Your OTP is Verified")

  else:
      b=tmsg.showinfo("Verification Failed","Please check your OTP Again")

#title label
l1=Label(frame,text="OTP GENERATOR",font="Times 20 bold",bg="grey")
l1.place(x=80,y=20)
l2=Label(frame,text="Enter your Email Adress: ",bg="grey",font="arial 11 bold").place(x=13,y=75)
l3=Label(frame,text="Enter your OTP: ",bg="grey",font="arial 11 bold").place(x=70,y=130)

#entry widgets
el2=StringVar()
entryl2=Entry(frame,textvariable=el2,borderwidth=3).place(x=192,y=75)
el3=StringVar()
entryl3=Entry(frame,textvariable=el3,borderwidth=3).place(x=192,y=130)

#buttons
but1=Button(text="Send",bg="grey",font="arial 9 bold",command=sending).place(x=327,y=75)
but2=Button(text="Verify",bg="grey",font="arial 9 bold",command=verification).place(x=327,y=130)

root.mainloop()