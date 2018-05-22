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
    
def cw (a, b, c):
    return bool((a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y)) < 0)

def ccw (a, b, c):
    return bool(((a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y)) > 0))

# Вычисление оболочки
def hull (a):
    if (len(a) == 1):
        return
    a.sort()
    p1 = Point(a[0].x,a[0].y)
    p2 = Point(a[len(a)-1].x,a[len(a)-1].y)
    up=[]
    down=[]
    up.append(p1)
    down.append(p1)
    for i in range(1,len(a)):
        if((i==len(a)-1) | cw (p1, a[i], p2)):
            while(len(up)>=2):
                if cw (up[len(up)-2], up[len(up)-1], a[i])==0:
                    up.pop()
                else:
                    break
            up.append(a[i])
        if((i==len(a)-1) | ccw (p1, a[i], p2)):
            while(len(down)>=2):
                if ccw ( down[len(down)-2] , down[len(down)-1], a[i])==0:
                    down.pop()
                else:
                    break
            down.append(a[i])
    a.clear();
    for i in range(0,len(up)):
        a.append(up[i])
    i=len(down)-2
    while(i>=0):
        a.append(down[i])
        i-=1


pt=[]
#-----------------------------
def getXY(event):
    global pt
    global canv
    a=Point(event.x_root,event.y_root)
    pt.append(a)
    update()
    
def Exit(event):
    global root
    root.destroy()
    
def Back(event):
    global pt
    if(len(pt)>=0):
        pt.pop()
    update()
    
def update():
    global c
    global pt
    global canv
    canv.delete("all")
    for i in range(0,len(pt)):
        canv.create_oval(pt[i].x-3, pt[i].y-3, pt[i].x+3, pt[i].y+3, outline="red", fill="red", width=0)
    c=[]
    c.extend(pt)
    hull(c)
    for i in range(1,len(c)):
        canv.create_line(c[i-1].x,c[i-1].y,c[i].x,c[i].y,width=2,fill="green") 
    canv.create_line(c[len(c)-1].x,c[len(c)-1].y,c[0].x,c[0].y,fill="green")
    canv.pack()
    
root = Tk()
root.attributes("-fullscreen", True)
canv = Canvas(root, width = SizeX, height = SizeY, bg = "white")
canv.pack()
root.bind('<Button-1>', getXY)
root.bind('<Return>',Exit)
root.bind('<Control-z>', Back)
root.mainloop()
