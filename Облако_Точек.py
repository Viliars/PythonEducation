import random
import math
from tkinter import *
#------------------------

class Point:
    def __init__(self,x,y,id):
        self.x=x;
        self.y=y;
        self.id=id;
    def __str__(self):
        return str(self.x)+' '+str(self.y)+' '+str(self.id)
    def __lt__(self,other):
        return (self.x<other.x)|((self.x==other.x)&(self.y<other.y))
def cmp_x(self,other):
    return (self.x<other.x)|((self.x==other.x)&(self.y<other.y))
def cmp_y(self,other):
    return self.y<other.y;
def upd_ans(a,b):
    global ansa
    global ansb
    global mindist
    dist=math.sqrt((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y))
    if(dist<mindist):
        mindist=dist
        ansa=a.id
        ansb=b.id
def rec(l,r):
    global mindist
    global ansa
    global ansb
    if(r-l<=3):
        for i in range(l,r+1):
            for j in range(i+1,r+1):
                upd_ans(c[i],c[j])
        Point.__lt__=cmp_y
        c[l:r+1]=sorted(c[l:r+1])
        Point.__lt__=cmp_x
        return
    m=(l+r)//2
    midx=c[m].x;
    rec(l,m)
    rec(m+1,r)
    Point.__lt__=cmp_y
    t.sort()                #??????
    Point.__lt__=cmp_x
    c[l:r+1]=t[0:r-l+1]       #?????
    #-----------------
    tsz=0
    for i in range(l,r+1):
        if(abs(c[i].x-midx)<mindist):
            j=tsz-1
            while((j>=0)&((c[i].y-t[j].y)<mindist)):
                j-=1
                upd_ans(c[i],t[j])
            t[tsz]=c[i]
            tsz+=1
            
mindist=100000.0
t=[]
c=[]
ansa=0
ansb=0
root = Tk()
canv = Canvas(root, width = 1000, height = 1000, bg = "white")
canv.create_line(500,1000,500,0,width=2,arrow=LAST) 
canv.create_line(0,500,1000,500,width=2,arrow=LAST)
for i in range(0,300):
    a=Point(random.uniform(-500,500),random.uniform(-500,500),i)
    canv.create_oval(a.x-3+500, a.y-3+500, a.x+3+500, a.y+3+500, outline="red", 
        fill="red", width=0)
    c.append(a)
c.sort()
rec(0,299)



canv.create_oval(c[ansa].x-5+500, c[ansa].y-5+500, c[ansa].x+5+500, c[ansa].y+5+500, outline="red", 
        fill="green", width=0)
canv.create_oval(c[ansb].x-5+500, c[ansb].y-5+500, c[ansb].x+5+500, c[ansb].y+5+500, outline="red", 
        fill="green", width=0)

canv.pack()	
root.mainloop()

#test

test=[9,8,7,6,5,4,3,2,1]
testi=test
testi[4:7]=sorted(test[4:7])
print(testi)

              
