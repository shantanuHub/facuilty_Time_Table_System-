from Tkinter import *

top=Tk()
top.config(background="brown4")
top.title("WELCOME")
top.geometry("1600x900")














    


Label(top,text="SUBJECT NAME=",fg="black",bg="brown4",bd=14,font=("times",27)).place(x=300,y=215)

el=Entry(top,font=("arial",21))
el.place(x=690,y=230)

Button(top,text="submit ",fg="white",bg="cyan4",bd=10,padx=5,pady=5).place(x=690,y=390)
Button(top,text="cancel",fg="white",bg="cyan4",command=top.destroy,bd=10,padx=5,pady=5).place(x=830,y=390)




top.mainloop()







