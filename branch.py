from Tkinter import *
import ttk

top=Tk()
top.config(background="cyan4")
top.title("WELCOME")
top.geometry("1600x900")




combo=ttk.Combobox(top,font=('arial',30),values=("cs","it","ce","me","ec","ee"))
combo.set("select")
combo.place(x=690,y=320)

Label(top,text="BRANCH=",bg="cyan4",fg="black",bd=15,font=("times",30)).place(x=300,y=300)


Button(top,text="submit ",fg="black",bg="cyan2",bd=10,padx=5,pady=5).place(x=690,y=390)
Button(top,text="cancel",fg="black",bg="cyan2",bd=10,padx=5,pady=5).place(x=830,y=390)




top.mainloop()







