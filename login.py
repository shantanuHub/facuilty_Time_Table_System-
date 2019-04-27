from Tkinter import *
import tkMessageBox
import mysql.connector

top=Tk()
top.config(background="brown4")
top.title("WELCOME")
top.geometry("1600x900")


def login():
    
    

    conn=mysql.connector.connect(user="root",password="",host="localhost",database="class")
    cursor=conn.cursor()
    if(e1.get()==("") or e2.get()==("")):
        tkMessageBox.showinfo("alert","fill all feild first")
    elif(e1.get()==("admin") and e2.get()==("admin")):
        
        top.destroy()
        import  admin_welcome_page
        
    else:
        cursor.execute("select * from signin where user_id='"+e1.get()+"' and password='"+e2.get()+"'")

        if(cursor.fetchone()):
            top.destroy()
            import faculty_welcome
           
        else:
            tkMessageBox.showinfo("alert","id and password is not correct")







    


Label(top,text="USER ID     =",fg="white",bg="brown4",bd=13,font=("times",30)).place(x=300,y=220)
Label(top,text="PASSWORD     =",bg="brown4",fg="white",bd=13,font=("times",30)).place(x=300,y=300)
e1=Entry(top,bg="brown2",font=("arial",21))
e1.place(x=690,y=230)
e2=Entry(top,show="*",bg="brown2",font=("arial",21))
e2.place(x=690,y=320)
Button(top,text="Login ",fg="white",command=login,bg="crimson",bd=10,padx=5,pady=5).place(x=690,y=390)
Button(top,text="cancel",fg="white",command=top.destroy,bg="crimson",bd=10,padx=5,pady=5).place(x=830,y=390)




top.mainloop()







