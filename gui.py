import tkinter as tk

window=tk.Tk()#construct called
displayWidth=window.winfo_screenwidth()
displayHeight=window.winfo_screenheight()
width=200
height=200

left=int((displayWidth/2)- (width/2))
top=int((displayHeight/2)-(height/2))
window.geometry(f"{width}x{height}+{left}+{top}")
window.title("Tdo app")
window.iconbitmap("icon.ico")
window.resizable(False,False)




#run the window
window.mainloop()