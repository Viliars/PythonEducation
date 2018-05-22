import numpy as np
import cv2
#import argparse
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

def convex_hull (a):
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



#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "path to the image file")
#args = vars(ap.parse_args())


#image = cv2.imread(args["image"])



start = cv2.imread("1.jpg")

final = 1000
r = float(final)/start.shape[1]
dim = (final,int(start.shape[0]*r))


image = cv2.resize(start, dim)

low = (50,10,50)
high = (200,70,250)
only = cv2.inRange(image, low, high)


kernel = np.ones((5,5),np.uint8)

#kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
#opening = cv2.morphologyEx(buf, cv2.MORPH_CLOSE, kernel2)


only2 = cv2.dilate(only,kernel,iterations = 3)

se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
mask = cv2.morphologyEx(only2, cv2.MORPH_CLOSE, se1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)



dilation = cv2.dilate(opening,kernel,iterations = 2)



moments = cv2.moments(dilation, 1) 
x_moment = moments['m10']
y_moment = moments['m01']
area = moments['m00']
x = int(x_moment / area) 
y = int(y_moment / area) 


(_ , cnts, _ ) = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


midx=0
midy=0
array=[]
mindist=100000.0
for x in cnts:
    midx=0
    midy=0
    for y in x:
        midx+=y[0][0]
        midy+=y[0][1]
    midx//=len(x)
    midy//=len(x)
    p=Point(midx,midy)
    array.append(p)

#---------------------------------------------   
convex_hull(array)

    
hull=[]
for x in array:
    hull.append([x.x,x.y])


der = np.array(hull)


c=[0 for i in range(len(cnts))]
rect=[0 for i in range(len(cnts))]
box=[0 for i in range(len(cnts))]
for i in range(len(cnts)):
    c[i] = sorted(cnts, key = cv2.contourArea, reverse = True)[i]
    rect[i] = cv2.minAreaRect(c[i])
    box[i] = np.int0(cv2.boxPoints(rect[i]))




cv2.drawContours(image, [der] , -1, (0, 255, 0), 3)
 
cv2.imshow('Found', image)
cv2.waitKey(0)
