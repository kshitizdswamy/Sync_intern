from tkinter import *
import pyperclip
import pyshorteners

root= Tk()
root.title("url shortener")
root.geometry("500x250")

def shorty():
    url= entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    entry2.insert(END,s)

def copy():
    pyperclip.copy(entry2.get())

#main_frame
main_body=Frame(root,height=250,width=500,bg="beige")
main_body.pack()

#all_labels
l1=Label(main_body,text="Enter your url below",font=("system 20 bold"),bg="beige")
l1.place(x=110,y=25)

#entry_widgets
entry1=Entry(main_body,width=35,borderwidth=2,font=("ariel 12 bold"))
entry1.place(x=50,y=80)
entry2=Entry(main_body,width=35,borderwidth=2,font=("ariel 12 bold"))
entry2.place(x=50,y=150)

#buttons
but1=Button(main_body,text="Shorten url",font=("ariel 9 bold"),command=shorty,bg="green",fg="white")
but1.place(x=380,y=78)
but2=Button(main_body,text="Copy url",font=("ariel 9 bold"),bg="green",fg="white",command=copy)
but2.place(x=380,y=148)

root.mainloop()