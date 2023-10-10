
from tkinter import *

root=Tk()
root.title("Chatbot")
root.geometry("500x500")
root.configure(bg="beige")

#function_declaration
xi=0
yi=0

def clear():
    global yi
    yi -=yi
    for widget in text.winfo_children():
        widget.destroy()
    yi -=50

def send(event):
    global yi
    user_ent=entry.get()
    use=Label(text,width=51,text="You >> "+user_ent,font="times 12", bg="chartreuse3",anchor="e")
    use.place(x=xi,y=yi)
    if 'hello' in user_ent:
        bot = Label(text, width=51, text="Atlas >> hey bud! :)", font="times 12", bg="green yellow", anchor="w")
        bot.place(x=xi, y=yi+25)
    elif 'created' in user_ent:
        bot = Label(text, width=51, text="Atlas >> I was created by Kshitiz for helping gym beginners", font="times 12", bg="green yellow", anchor="w")
        bot.place(x=xi, y=yi + 25)
    elif 'developed' in user_ent:
        bot = Label(text, width=51, text="Atlas >> I was created by Kshitiz for helping gym beginners", font="times 12", bg="green yellow", anchor="w")
        bot.place(x=xi, y=yi + 25)
    elif 'how can you help me' in user_ent:
        bot = Label(text, width=51, text="Atlas >> i can help you by giving some bro tips that you can implement in\nyour fitness journey", font="times 12", bg="green yellow", anchor="w")
        bot.place(x=xi, y=yi + 25)
    elif 'what should i do to gain weight in the beginning' in user_ent:
        bot = Label(text, width=51, text="Atlas >> Gaining weight in a healthy and controlled manner is important to\nensure that you're adding muscle mass and not just accumulating excess fat.\nHere are some tips to help you gain weight effectively:\n1.Increase Caloric Intake, To gain weight, you need to consume\nmore calories than your body burns\n2.Protein Intake,Protein is essential for building muscle.\nInclude good sources of protein in your diet\n3.Be Patient: Gaining weight in a healthy way takes time. Aim for a gradual\n and sustainable weight gain of about 0.2 to 0.45 kg per week.", font="times 12", bg="green yellow", anchor="w")
        bot.place(x=xi, y=yi + 25)
    elif 'if i am not getting any results then what to do' in user_ent:
        bot = Label(text, width=51, text="Atlas >> Remember that gaining weight, especially in a healthy and controlled\nmanner,can take time. Be patient with yourself and stay consistent\nwith your efforts", font="times 12", bg="green yellow", anchor="w")
        bot.place(x=xi, y=yi + 25)
    elif 'how to cope up with demotivation' in user_ent:
        bot = Label(text, width=51, text="Atlas >> Remember that motivation can be fleeting, and it's natural to\nexperience highs and lows. The key is to build habits and strategies that help\n you stay committed and continue working towards your goals even when\nmotivation is low.", font="times 12", bg="green yellow", anchor="w")
        bot.place(x=xi, y=yi + 25)
    elif 'atlas do you beleive in me' in user_ent:
        bot = Label(text, width=51, text="Atlas >> yes i do mate! I'm here to provide information, answer questions,\nand assist you to the best of my abilities.", font="times 12", bg="green yellow", anchor="w")
        bot.place(x=xi, y=yi + 25)
    elif user_ent == 'clear':
        clear()
    else:
        bot = Label(text, width=51, text="Atlas >> stay focused bro..I'd only answer gym related stuff ", font="times 12", bg="green yellow", anchor="w")
        bot.place(x=xi, y=yi+25)
    yi+=50

#design_layout
can_wid= Canvas(root,height=90,width=500,bg="beige")
can_wid.pack()
can_wid.create_rectangle(50,5,450,90,outline="green",fill="green")
can_wid.create_oval(90,90,2,5,outline="green",fill="green")
can_wid.create_oval(497,90,400,5,outline="green",fill="green")

#title
title=Label(root,text="ATLAS",font="system 33 bold",bg="green")
title.place(x=185,y=10)
moto=Label(root,text="Personal GYM bro",font="system 10 bold",bg="green")
moto.place(x=185,y=63)

#scrollbar_and_main_chat_display_box
v=Scrollbar(root, orient='vertical',bg="beige")
v.place(x=480,y=100,height=322)
text= Text(root,font="arial 9 bold",bg="beige",yscrollcommand=v.set)
text.place(x=10,y=100,width=470,height=320)
v.config(command=text.yview)

#user_input_area
entry=Entry(root,font="times 15 ")
entry.place(x=10,y=429,width=400,height=50)

#send_button
btn = Button(root,text="Send",font="arial 15 bold",bg="green",highlightbackground="green")
root.bind("<Return>",send)
btn.place(x=420,y=430,height=50)

#credits
cred=Label(root,text="version 1.00",font="arial 10 bold")
cred.place(x=10,y=480)

root.mainloop()