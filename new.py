from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.title("login")
tk.geometry("400x300")
tk.resizable(False, False)
tk.configure(bg="black")


def login():
    username = entry1.get()
    password = entry2.get()

    if username == "" and password == "":
        messagebox.showerror("Error", "Please enter the username and password")
    elif username == "":
        messagebox.showinfo("Error", "Please enter username")
    elif password == "":
        messagebox.showinfo("Error", "Please Enter the password")
    elif username == "Vaishnavi" and password == "baisvaishnavi7":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Oops", "Invalid username or password")


# Label
Label(tk, text="CyberSharks", font="impack 20 bold", bg="black", fg="green").pack()
Label(tk, text="username").place(x=100, y=140)
Label(tk, text="Password").place(x=100, y=170)

# Entry
entry1 = Entry(tk, bd=3)
entry1.place(x=170, y=131)
entry2 = Entry(tk, bd=3, show="*")
entry2.place(x=170, y=170)

# Button
Button(tk, text="Login", fg="green", bg="black", command=login).place(x=160, y=210)

# Scrollbar and Listbox
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set, width=130)

for i in range(100):
    mylist.insert(END, 'This is the line number ' + str(i))

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

mainloop()
