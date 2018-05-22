# <head>
# -- SetA--
SizeX=1600
SizeY=900
# -- --

import random
from tkinter import *
# Класс Точка
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self,other):
        return bool((self.x<other.x)|((self.x==other.x)&(self.y<other.y)))
    def __str__(self):
        return str(self.x)+' '+str(self.y)
    
#-----------------------------
    
def Exit(event):
    global root
    root.destroy()
    
    
class Line:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c


 
EPS = 0.0001
 
def det (a,b,c,d):
    return (a * d - b * c)

def between (a,b,c):
    if(min(a,b) <= c + EPS) & (c <= max(a,b) + EPS):
        return True
    else:
        return False


def inter (a, b, c, d):
    if (a > b):
        a,b=b,a
    if (c > d):
        c,d=d,c
    if(max(a,c) <= min(b,d)):
        return True
    else:
        return False


def answering ():
    global a
    global b
    global c
    global d
    global answer
    A1 = a.y-b.y
    B1 = b.x-a.x
    C1 = -A1*a.x - B1*a.y
    A2 = c.y-d.y
    B2 = d.x-c.x
    C2 = -A2*c.x - B2*c.y
    zn = det (A1, B1, A2, B2);
    if (zn != 0):
        answer.x = - det (C1, B1, C2, B2)/ zn
        answer.y = - det (A1, C1, A2, C2)/ zn
        if(between(a.x, b.x, answer.x) & between (a.y, b.y, answer.y) & between (c.x, d.x, answer.x) & between (c.y, d.y, answer.y)):
            return True
        else:
            return False
    else:
        if((det (A1, C1, A2, C2) == 0) & (det (B1, C1, B2, C2) == 0) & inter (a.x, b.x, c.x, d.x) & inter (a.y, b.y, c.y, d.y)):
            return True
        else:
            return False

def one(event):
    global flag1
    global flag2
    global flag3
    global flag4
    flag1=True
    flag2=False
    flag3=False
    flag4=False

def two(event):
    global flag1
    global flag2
    global flag3
    global flag4
    flag1=False
    flag2=True
    flag3=False
    flag4=False

def tree(event):
    global flag1
    global flag2
    global flag3
    global flag4
    flag1=False
    flag2=False
    flag3=True
    flag4=False

def four(event):
    global flag1
    global flag2
    global flag3
    global flag4
    flag1=False
    flag2=False
    flag3=False
    flag4=True


def getXY(event):
    global a
    global b
    global c
    global d
    if(flag1):
        a=Point(event.x_root,event.y_root)
    if(flag2):
        b=Point(event.x_root,event.y_root)
    if(flag3):
        c=Point(event.x_root,event.y_root)
    if(flag4):
        d=Point(event.x_root,event.y_root)
    update()


def update():
    global ans
    global canv
    global a
    global b
    global c
    global d
    run()
    canv.delete("all")
    canv.create_oval(a.x-3, a.y-3, a.x+3, a.y+3, outline="blue", fill="blue", width=0)
    canv.create_oval(b.x-3, b.y-3, b.x+3, b.y+3, outline="blue", fill="blue", width=0)
    canv.create_oval(c.x-3, c.y-3, c.x+3, c.y+3, outline="blue", fill="blue", width=0)
    canv.create_oval(d.x-3, d.y-3, d.x+3, d.y+3, outline="blue", fill="blue", width=0)
    canv.create_line(a.x,a.y,b.x,b.y,width=2,fill="green")
    canv.create_line(c.x,c.y,d.x,d.y,width=2,fill="green")
    canv.create_text(a.x,a.y,text="A",anchor="nw",font=("Purisa", 15),fill="red")
    canv.create_text(b.x,b.y,text="B",anchor="nw",font=("Purisa", 15),fill="red")
    canv.create_text(c.x,c.y,text="C",anchor="nw",font=("Purisa", 15),fill="red")
    canv.create_text(d.x,d.y,text="D",anchor="nw",font=("Purisa", 15),fill="red")
    if ans:
        canv.create_text(100,100,text="YES",font=("Purisa", 20),fill="red")
        canv.create_oval(answer.x-5, answer.y-5, answer.x+5, answer.y+5, outline="red", fill="red", width=0)
    else:
        canv.create_text(100,100,text="NO",font=("Purisa", 20),fill="red")
    canv.pack()

def run():
    global line1
    global line2
    global ans
    A1 = a.y-b.y
    B1 = b.x-a.x
    C1 = -A1*a.x - B1*a.y
    A2 = c.y-d.y
    B2 = d.x-c.x
    C2 = -A2*c.x - B2*c.y
    line1=Line(A1,B1,C1)
    line2=Line(A2,B2,C2)
    if answering():
        ans=True 
    else:
        ans=False


a=Point(100.0,498.0)
b=Point(236.0,540.0)
c=Point(858.0,533.0)
d=Point(200.0,333.0)
flag1=False
flag2=False
flag3=False
flag4=False
ans=False
answer=Point(0,0)

root = Tk()
root.attributes("-fullscreen", True)
canv = Canvas(root, width = SizeX, height = SizeY, bg = "white")
update()
root.bind('<Motion>', getXY)
root.bind('<Return>',Exit)
root.bind('<a>', one)
root.bind('<b>', two)
root.bind('<c>', tree)
root.bind('<d>', four)
root.mainloop()

