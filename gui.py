import tkinter as tk
from tkinter import ttk 

window=tk.Tk()#construct called
displayWidth=window.winfo_screenwidth()
displayHeight=window.winfo_screenheight()
width=400
height=400

left=int((displayWidth/2)- (width/2))
top=int((displayHeight/2)-(height/2))
window.geometry(f"{width}x{height}+{left}+{top}")
window.title("Tdo app")
window.iconbitmap("icon.ico")
window.resizable(False,False)

entryField=ttk.Entry(window)
entryField.pack()

#oldButton=tk.Button(window,text="old button")
#oldButton.pack()
def ButtonClick():
    out=entryField.get()
    label.configure(text=out)
    
   # newButton.configure(state="disable")    #disable in after click


newButton=ttk.Button(window,text="latest button",command=ButtonClick)
newButton.pack()

label=ttk.Label(window,text="text")
label.pack()

#run the window
window.mainloop()