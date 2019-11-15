import numpy as np
import cv2

def findBox(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret,thresh = cv2.threshold(gray,127,255,1)
    
    contours,h = cv2.findContours(thresh,1,2)

    k = 0
    
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        if len(approx)==4:
            if len(cnt)>300:
                result = cnt
                k = k+1
    if k != 1 :
        print("Error")
        return 1
    return result


def sliceImage(img):
    a = findBox(img)

    x = []
    y = []
    for i in a:
        x.append(i[0][0])
        y.append(i[0][1])

    #보정값

    addY = int((max(y)-min(y))/10)
    addX = int((max(x)-min(y))/5)
    img = img[min(y)-addY:max(y), min(x)-addX:max(x)+addX]
    return img