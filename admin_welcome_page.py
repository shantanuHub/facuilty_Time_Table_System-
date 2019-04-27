
from Tkinter import*

top=Tk()
top.title("welcome page")
top.geometry("1590x900+0+0")
top.configure(background="brown4")

def reg():
    top.destroy()
    import registration_form
    
def sub1():
    top.destroy()
    import subject1
    
def bch():
    top.destroy()
    import branch
def area():
    top.destroy()
    import Selection_Area2

    
menubar=Menu(top)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="FACULTY",menu=filemenu)
filemenu.add_command(label="add",command=reg)                                        
filemenu.add_command(label="list")
filemenu.add_separator()

filemenu.add_command(label="Exit",command=top.quit)



editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="SUBJECT",menu=editmenu)
editmenu.add_command(label="add",command=sub1)


helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="BRANCH",menu=helpmenu)
helpmenu.add_command(label="add",command=bch)

timemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="TIME TABLE",menu=timemenu)
timemenu.add_command(label="add",command=area)


logmenu=Menu(menubar)
menubar.add_cascade(label="LOGOUT",menu=logmenu)



top.config(menu=menubar)

top.mainloop()
