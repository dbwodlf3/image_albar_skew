import numpy as np
import cv2
import rotate as rt

#unicode 문제
def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode="w+b") as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

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

def process(fileName, saveFolder):
    stream = open(u'%s'%fileName, "rb")
    bytes = bytearray(stream.read())
    numpyarray = np.asarray(bytes, dtype=np.uint8)
    bgrImage = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)

    img = bgrImage
    k = sliceImage(img)
    k = rt.getRotation(k)

    fileName = os.path.split(fileName)[1]
    saveName = os.path.join(saveFolder, "converted_%s"%fileName)
    imwrite("%s"%saveName, k)
    #cv2.waitKey(0)

## main

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(BASE_DIR, "테스트")
SAVE_DIR = os.path.join(BASE_DIR, "end")

try:
    os.mkdir(SAVE_DIR)
except:
    pass

# Create your views here.


files = [f for f in os.listdir(FILE_DIR) if os.path.isfile(os.path.join(FILE_DIR, f))]

process_file = os.path.join(FILE_DIR, files[0])

test_path = os.path.join(BASE_DIR, "한글.jpg")
process("%s"%test_path, SAVE_DIR)



#for i in files:
    #file_path = os.path.join(FILE_DIR, i)
    #process("%s"%file_path, SAVE_DIR)
    #process("%s"%file_path, SAVE_DIR)