from tkinter import *
from tkinter import messagebox

t=Tk()
t.geometry("425x350")
def login():
    f2=Frame(bg="#091e42")
    f2.place(x=0,y=0,width=425,height=350)

    u=Label(f2,text="LogIn Page",bg="#091e42",fg="white")
    u.place(x=150,y=10)

    u1=Label(f2,text="Enter Name",bg="#091e42",fg="white")
    u1.place(x=100,y=80)
    e1=Entry(f2,font=("",12))
    e1.place(x=200,y=80,width=120)

    u2=Label(f2,text="Enter Password",bg="#091e42",fg="white")
    u2.place(x=100,y=130)
    e2=Entry(f2,font=("",12),show='*')
    e2.place(x=200,y=130,width=120)

    b3=Button(f2,text="LogIn")
    b3.place(x=150,y=200,width=80,height=40)

    b2=Button(f2,text="<-",command=home)
    b2.place(x=2,y=3)
    
    


    """e1=Entry(f2)
    e1.pack()
    e2=Entry(f2)
    e2.pack()
    b2=Button(f2,text="back" ,command=home)
    b2.pack()
    b3=Button(f2,text="LogIn")
    b3.pack()"""
def SignIn():
    f3=Frame(bg="#091e42")
    f3.place(x=0,y=0,width=425,height=350)

    u=Label(f3,text="SignIn Page",bg="#091e42",fg="white")
    u.place(x=150,y=10)

    u1=Label(f3,text="Enter Name",bg="#091e42",fg="white")
    u1.place(x=100,y=80)
    e1=Entry(f3,font=("",12))
    e1.place(x=200,y=80,width=120)

    u2=Label(f3,text="Enter Pass",bg="#091e42",fg="white")
    u2.place(x=100,y=130)
    
    e2=Entry(f3,font=("",12),show='*')
    e2.place(x=200,y=130,width=120)

    u3=Label(f3,text="Enter C. Pass",bg="#091e42",fg="white")
    u3.place(x=100,y=130)

    e3=Entry(f3,font=("",12),show='*')
    e3.place(x=200,y=130,width=120)

    b3=Button(f3,text="SignIn")
    b3.place(x=150,y=250,width=80,height=40)

    b2=Button(f3,text="<-",command=home)
    b2.place(x=2,y=3)



    """e1=Entry(f3)
    e1.pack()
    e2=Entry(f3)
    e2.pack()
    e3=Entry(f3)
    e3.pack()
    b2=Button(f3,text="back" ,command=home)
    b2.pack()
    b3=Button(f3,text="SignIn")
    b3.pack()   """
    
    
def home():
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=425,height=350)
    b1=Button(f1,text="LogIn" , command =login)
    b1.place(x=100,y=50,width=80,height=40)
    b2=Button(f1,text="SignIn" , command =SignIn)
    b2.place(x=200,y=50,width=80,height=40)
home()
t.mainloop()

"""
tk= Tk()
tk.title("login")
tk.geometry("400x300")
tk.resizable(False,False)
tk.configure(bg="black")
def login():
    username=entry1.get()
    password=entry2.get()
    if(username=="" and password==""):
        messagebox.showerror("Error","Please enter the username and password")
    elif(username==""):
        messagebox.showinfo("Error","Please enter username")
    elif(password==""):
        messagebox.showinfo("Error","Please Enter the password")
    elif(username=="Vaishnavi" and password=="baisvaishnavi7"):
        messagebox.showinfo("Success","Login SUccessfull")
        
    else:
        messagebox.showerror("Oops","Invalid username?password")
        

    
    
#Label
Label(tk,text="CyberSharks",font="impack 20 bold",bg="black",fg="green").pack()
Label(tk,text="username").place(x=100,y=140)
Label(tk,text="Password").place(x=100,y=170)
#Entry

entry1=Entry(tk,bd=3)
entry1.place(x=170,y=131)
entry2=Entry(tk,bd=3,show="*")
entry2.place(x=170,y=170)
#button
Button(tk,text="Login",fg="green",bg="black",command=login).place(x=160,y=210)


mainloop()




root=Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill =Y)

mylist = Listbox(root, yscrollcommand = scrollbar. set, width = 130)

for i in range(100):
    mylist.insert(END, 'This is the line number' + str(i))
    
    mylist.pack( side = LEFT , fill =BOTH)
    
    scrollbar.config( command = mylist.yview)
    
    mainloop()
"""