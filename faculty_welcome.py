
from Tkinter import*

top=Tk()
top.title("faculty welcome")
top.geometry("1590x900+0+0")
top.configure(background="darkorchid3")


Label(top,text="WELCOME FACULTIES",width=90,height=20,font=("poiret",20,"bold"),bg="darkorchid4",fg="white").place(x=1,y=30)


menubar=Menu(top)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="schedule",menu=filemenu)
filemenu.add_command(label="")
filemenu.add_command(label="")
filemenu.add_command(label="")

filemenu.add_separator()

filemenu.add_command(label="Exit",command=top.quit)



editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="logout",menu=editmenu)
editmenu.add_command(label="undo")




top.config(menu=menubar)

top.mainloop()
