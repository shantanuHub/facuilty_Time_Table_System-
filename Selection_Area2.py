from Tkinter import *
import ttk
import mysql.connector
top=Tk()
top.config(background="cyan4")
top.title("Time Table Generator")
top.geometry("1600x900+0+0")

def faculty():
    conn=mysql.connector.connect(user="root",password="",host="localhost",database="class")
    cursor=conn.cursor()
    cursor.execute("insert into time_table(subject,branch,semister,faculty,period,time) values('"+e1.get()+"','"+e2.get()+"','"+e3.get()+"','"+e4.get()+"','"+e5.get()+"','"+e6.get()+"')")
    top.destroy()
    import Selection_Area2
    



conn=mysql.connector.connect(user="root",password="",host="localhost",database="class")
cursor=conn.cursor()
cursor.execute("select first_name,last_name from signin")
list=[]
for i in cursor.fetchall():
    
    list.append(i[0]+" "+i[1])

Label(top,text="Select",bg="cadetblue3",fg="dodgerblue4",font=("comic sans MS",30,"underline",)).place(x=500,y=20)

Label(top,text="Select Subject",bg="cadetblue3",fg="dodgerblue4",font=("comic sans MS",20,)).place(x=270,y=200)
var=StringVar(top)
var.set("Please Select")
option=OptionMenu(top,var,"OS","TOC","ADDA","CSO","DISCRETE STR","DATA STRUCTURE")
option.place(x=550,y=200)

Label(top,text="Select Branch",bg="cadetblue3",fg="dodgerblue4",font=("comic sans MS",20)).place(x=270,y=250)
var=StringVar(top)
var.set("Please Select")
option=OptionMenu(top,var,"CS","IT","ME","CIVIL","EE","ECE")
option.place(x=550,y=250)

Label(top,text="Select Semester",bg="cadetblue3",fg="dodgerblue4",font=("comic sans MS",20,)).place(x=270,y=300)
var=StringVar(top)
var.set("Please Select")
option=OptionMenu(top,var,"1ST","2ND","3RD","4TH","5TH","6TH","7TH","8TH")
option.place(x=550,y=300)

Label(top,text="Select Faculty",bg="cadetblue3",fg="dodgerblue4",font=("comic sans MS",20)).place(x=270,y=350)
var=StringVar(top)
var.set("Please Select")
option=OptionMenu(top,var,*list)
option.place(x=550,y=350)

Label(top,text="Select Period",bg="cadetblue3",fg="dodgerblue4",font=("comic sans MS",20,)).place(x=270,y=400)
var=StringVar(top)
var.set("Please Select")
option=OptionMenu(top,var,"1ST","2ND","3RD","4TH","5TH","6TH")
option.place(x=550,y=400)

Label(top,text="Time",bg="cadetblue3",fg="dodgerblue4",font=("comic sans MS",20)).place(x=270,y=450)
var=StringVar(top)
var.set("Please Select")
option=OptionMenu(top,var,"9:30-10:30","10:30-11:30","11:30-12:30","1:00-2:00","2:00-3:00","3:00-4:00")
option.place(x=550,y=450)

Button(top,text="Submit", bd=4, fg= "grey",command=faculty, font= ('comic sans MS',10,'bold'),bg="dodgerblue4").place(x=480,y=550)
Button(top,text="Cancel", bd=4, fg= "grey", font= ('comic sans MS',10,'bold'),bg="dodgerblue4").place(x=650,y=550)


top.mainloop()
