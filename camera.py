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



#-------------------------------
        # Second frame
def update(a):
    pass


        
cv2.namedWindow( "settings" )
cv2.createTrackbar('h1', 'settings', 0, 255, update)
cv2.createTrackbar('s1', 'settings', 0, 255, update)
cv2.createTrackbar('v1', 'settings', 0, 255, update)
cv2.createTrackbar('h2', 'settings', 255, 255, update)
cv2.createTrackbar('s2', 'settings', 255, 255, update)
cv2.createTrackbar('v2', 'settings', 255, 255, update)





#low2=(190,190,190)
#high2=(255,255,255)
#temp = cv2.imread("point.jpg")
#buf = cv2.inRange(temp, low2, high2)
#kernel2 = np.ones((5,5),np.uint8)
#bufer = cv2.erode(buf,kernel2,iterations = 1)
#find = cv2.dilate(bufer ,kernel2,iterations = 2)
low2=(20,20,20)
high2=(80,80,80)
vc = cv2.VideoCapture(0)

if vc.isOpened(): 
    rval, frame = vc.read()
else:
    rval = False

while rval:
    closed=0
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27:
        break
    try:
        h1 = cv2.getTrackbarPos('h1', 'settings')
        v1 = cv2.getTrackbarPos('v1', 'settings')
        s1 = cv2.getTrackbarPos('s1', 'settings')
        h2 = cv2.getTrackbarPos('h2', 'settings')
        s2 = cv2.getTrackbarPos('s2', 'settings')
        v2 = cv2.getTrackbarPos('v2', 'settings')
        low2 = (h1,s1,v1)
        high2 = (h2,s2,v2)
        only = cv2.inRange(frame, low2, high2)
        
        #result = cv2.matchTemplate(only,find,cv2.TM_SQDIFF)
        #print(result)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        kernel2 = np.ones((2,2),np.uint8)
        closed = cv2.morphologyEx(only, cv2.MORPH_CLOSE, kernel)
        buf = cv2.erode(closed,kernel2,iterations = 1)
        dilation = cv2.dilate(closed ,kernel,iterations = 4)



        #moments = cv2.moments(dilation, 1) 
        #x_moment = moments['m10']
        #y_moment = moments['m01']
        #area = moments['m00']
        #x = int(x_moment / area) 
        #y = int(y_moment / area)


        (_ , cnts, _ ) = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        midx=0
        midy=0
        array=[]
        
        for x in cnts:
            midx=0
            midy=0
            for y in x:
                midx+=y[0][0]
                midy+=y[0][1]
            midx//=len(x)
            midy//=len(x)
            flag=True
            for y in x:
                if((abs(midx-y[0][0])>20) | (abs(midy-y[0][1])>20)):
                    flag=False
                if(flag):
                    p=Point(midx,midy)
                    array.append(p)
        #---------------------------------------------   
        convex_hull(array)
            
        hull=[]
        for x in array:
            hull.append([x.x,x.y])


        der = np.array(hull)

        cv2.drawContours(frame, [der] , -1, (0, 255, 0), 3)
        cv2.imshow("Res", frame)
        cv2.imshow("Res2", dilation)
    except:
        pass
        
cv2.destroyAllWindows()
vc.release()
