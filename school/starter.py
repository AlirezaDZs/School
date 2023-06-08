import re
from tkinter import messagebox

def ppp(data):
    f = re.split("\*|\n", data)
    if f[-1]=="":
        f.pop()
    return f

def rewrite(list,name):
    f = open(f"{name}.txt","w")
    for i in range(0,len(list),2):
        reg = f"{list[i]}*{list[i+1]}\n"
        f.write(reg)
    f.close()

def getjob(us,ps):
    f = open("server.txt","r")
    global f2
    f2 = f.read()
    f2 = ppp(f2)
    f.close()
    isthere = False
    for i in range(1,len(f2),4):
        if us == f2[i] and ps == f2[i+2]:
            isthere = True
            global ind
            ind = i
            return f2[i+1]
    if not isthere:
        messagebox.showerror(title="ERROR!",message="The ID doesn't exist or password is wrong!")
        return

def tmaker(us,sc):
    global error
    error = False
    if int(sc) > 20 :
        messagebox.showerror(title="ERROR!",message="Score you entered is more than 20")
        error = True
        return
    elif int(sc) < 0 :
        messagebox.showerror(title="ERROR!",message="Score you entered is less than 20")
        error = True
        return
    isthere = False
    for i in range(len(f2)):
        if f2[i]==us:
            name = f2[i-1]
            isthere=True
            break
    if isthere==False:
        messagebox.showerror(title="ERROR!",message="The student doesn't exist!")
        error = True
        return
    try:
        f = open(f"{f2[ind-1]}.txt","r")
        f3 = f.read()
        f3 = ppp(f3)
        f.close()
        edit = False
        for i in range(len(f3)):
            if f3[i]==name:
                edit = True
                f3[i+1]=sc
                rewrite(f3, f2[ind-1])
                break
        if edit==False:
            f = open(f"{f2[ind-1]}.txt","a")
            reg = f"{name}*{sc}\n"
            f.write(reg)
            f.close()
    except FileNotFoundError:
        f = open(f"{f2[ind-1]}.txt","a")
        reg = f"{name}*{sc}\n"
        f.write(reg)
        f.close()

def display():
    try:
        f = open(f"{f2[ind-1]}.txt","r")
        f3 = f.read()
        f3 = ppp(f3)
        f.close()
        a = ""
        for i in range(0,len(f3),2):
            a += f"{f3[i]}\t{f3[i+1]}<br>-----------------------------<br>"
    except FileNotFoundError:
        a = "NO SCORE YET!"
    return a

def getname():
    return f2[ind-1]

def smaker(us,sc):
    if error==False:
        for i in range(len(f2)):
            if us == f2[i]:
                name = f2[i-1]
                break
        f = open("sub.txt","r")
        f3 = f.read()
        f.close()
        f3 = ppp(f3)
        for i in range(len(f3)):
            if f3[i]==f2[ind]:
                sub = f3[i+1]
                break
        f = open(f"{name}.txt","a")
        reg = f"{sub}*{sc}\n"
        f.write(reg)
        f.close()