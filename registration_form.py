from Tkinter import *
import tkMessageBox
import mysql.connector

top=Tk()
top.config(background="cyan4")
top.title("login window")
top.geometry("16000x900")

def login():
    
    conn=mysql.connector.connect(user="root",password="",host="localhost",database="class")
    cursor=conn.cursor()
    if(e1.get()==("") or e2.get()==("") or e3.get()==("") or e4.get()==("") or e5.get()==("") or e6.get()==("")):
        tkMessageBox.showinfo("alert","fill all feild first")
        
    else:
        cursor.execute("insert into signin(first_name,last_name,email,hometown,user_id,password) values('"+e1.get()+"','"+e2.get()+"','"+e3.get()+"','"+e4.get()+"','"+e5.get()+"','"+e6.get()+"')")
        conn.commit()

    top.destroy()
    import login




Label(top,text="ADD  DETAIL OF NEW FACULTY",fg="black",bg="cyan2",font="arial",width=70,height=30).place(x=700,y=20)
Label(top,text="FIRST NAME",bg="cyan4",fg="black",bd=14).place(x=100,y=80)
Label(top,text="LAST NAME",bg="cyan4",fg="black",bd=14).place(x=100,y=170)
Label(top,text="EMAIL ADDRESS",bg="cyan4",fg="black",bd=14).place(x=100,y=250)
Label(top,text="HOMETOWN",bg="cyan4",fg="black",bd=14).place(x=100,y=340)
Label(top,text="USER_ID",bg="cyan4",fg="black",bd=14).place(x=100,y=430)     
Label(top,text="PASSWORD",bg="cyan4",fg="black",bd=14).place(x=100,y=520)


e1=Entry(top,font="arial",bg="cyan2")
e1.place(x=300,y=80)
e2=Entry(top,font="italian",bg="cyan2")
e2.place(x=300,y=170)
e3=Entry(top,font="arial",bg="cyan2")
e3.place(x=300,y=250)

e4=Entry(top,font="arial",bg="cyan2")
e4.place(x=300,y=340)

e5=Entry(top,font="arial",bg="cyan2")
e5.place(x=300,y=430)


e6=Entry(top,show="*",font="arial",bg="cyan2")
e6.place(x=300,y=520)

Button(top,text="submit ",fg="black",bg="dodgerblue2",command=login,bd=10,padx=5,pady=5).place(x=300,y=580)
Button(top,text="cancel",fg="black",bg="dodgerblue2",bd=10,padx=5,pady=5).place(x=400,y=580)





top.mainloop()







