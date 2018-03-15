import random
from tkinter import *
import math
import time

time.clock()
imgx = 1580
imgy = 870
root = Tk()
canv = Canvas(root, width = imgx, height = imgy, bg = "white")



n = 200 # of cells

nx = [] 

ny = []

nr = []

ng = []

nb = []

for i in range(n):

    nx.append(random.randint(0, imgx - 1))

    ny.append(random.randint(0, imgy - 1))

    nr.append(random.randint(10, 99))

    ng.append(random.randint(10, 99))

    nb.append(random.randint(10, 99))



for y in range(imgy):

    for x in range(imgx):

        # find the closest cell center

        dmin = math.sqrt((imgx - 1)*(imgx-1)+(imgy - 1)*(imgy-1))

        j = -1

        for i in range(n):

            d = math.sqrt((nx[i] - x)*(nx[i] - x)+ (ny[i] - y)*(ny[i] - y))

            if d < dmin:

                dmin = d

                j = i

        
        canv.create_oval(x, y, x, y, outline="red", fill=("#"+str(nr[j])+str(ng[j])+str(nb[j])), width=0)



# mark the cell centers

for i in range(n):

    canv.create_oval(nx[i]-3, ny[i]-3, nx[i]+3, ny[i]+3, outline="black", 
        fill="black")
print(time.clock())
canv.pack()
print(time.clock())
root.mainloop()
