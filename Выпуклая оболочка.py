import random
from tkinter import *

class pt:
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

def convex_hull (a):
    if (len(a) == 1):
        return
    a.sort()
    p1 = pt(a[0].x,a[0].y)
    p2 = pt(a[len(a)-1].x,a[len(a)-1].y)
    canv.create_oval(p1.x-10+500, p1.y-10+500, p1.x+10+500, p1.y+10+500, outline="blue", fill="blue", width=0)
    canv.create_oval(p2.x-10+500, p2.y-10+500, p2.x+10+500, p2.y+10+500, outline="blue", fill="blue", width=0)
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


if(__name__=='__main__'):
    root = Tk()
    c=[]
    canv = Canvas(root, width = 1000, height = 1000, bg = "white")
    canv.create_line(500,1000,500,0,width=2,arrow=LAST) 
    canv.create_line(0,500,1000,500,width=2,arrow=LAST)

    key=300
    for i in range(0,50):
        a=pt(random.randint(-key,key),random.randint(-key,key))
        canv.create_oval(a.x-3+500, a.y-3+500, a.x+3+500, a.y+3+500, outline="red", fill="red", width=0)
        c.append(a)
    convex_hull(c)
    for i in range(1,len(c)):
        canv.create_oval(c[i].x-3+500, c[i].y-3+500, c[i].x+3+500, c[i].y+3+500, outline="blue", fill="blue", width=0)
        canv.create_line(c[i-1].x+500,c[i-1].y+500,c[i].x+500,c[i].y+500,width=2,arrow=LAST)
    canv.create_oval(c[0].x-3+500, c[0].y-3+500, c[0].x+3+500, c[0].y+3+500, outline="blue", fill="blue", width=0)   
    canv.create_line(c[len(c)-1].x+500,c[len(c)-1].y+500,c[0].x+500,c[0].y+500)
    canv.pack()	
    root.mainloop()


