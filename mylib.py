import numpy as np
import cv2

#해당 점의 시작점과 끝점을 알아야함. 같이 반환하자.

## Export Function

# input canny image
def getX(img):
    height = img.shape[0]
    width = img.shape[1]

    gap = 10
    counterX = gap
    before = 0
    item = [0]
    resultPoint = []

    start = (0,0) #(y,x)
    end = (0,0) # (y,x)
    startEndFlag = True
    ##값 인터벌을 넣어야 한다.
    for y in range(0, height):
        for x in range(0, width):
            #
            if img[y][x] > 1:
                if(startEndFlag):
                    start = (y, x)
                    startEndFlag = False
                item.append(0)
            elif counterX < 0:
                if(len(item)>10):
                    end = (y, x)
                    resultPoint.append((start, end, len(item)))
                #init
                start = (0,0)
                end = (0,0)
                item = [0]
                counterX = gap
                startEndFlag = True
            else :
                counterX = counterX - 1
    return resultPoint

def filterWidth(points, A , B):
    result = []
    for i in points:
        if (i[2]>=A and i[2]<=B):
            result.append(i)
    return result


def paintXAtoB(img,A,B):
    y0, x0 = A
    y1, x1 = B
    for y in range(y0,y1):
        for x in range(x0,x1):
            img[y][x] = (0, 255, 0)

# it is correct.
def paint(img):
    height = img.shape[0]
    width = img.shape[1]
    for y in range(0,100):
        for x in range(0,width):
            img[y][x] = 255