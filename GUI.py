from tkinter import *

from tkinter import scrolledtext

# Win conf
win = Tk()
win.title("MESSANGER")
win.geometry('350x550')
win.resizable(False, False)

# Message_Box
txt = scrolledtext.ScrolledText(win, width=40, height=30)
txt.grid(column=0, row=0)

# Entry
msg_input = Entry(win, font=("Arial", 14))
msg_input.grid(row=1,column=0,stic="we")

#SendButton

send_bt = Button(win,text="Send")
send_bt.grid(row=3,column=0,stick = "wesn")
win.mainloop()
