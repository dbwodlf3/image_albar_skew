import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)
minLineLength = 100
maxLineGap = 100

img = cv2.imread("test2.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
img_canny = cv2.Canny(img_gray, 50, 200, apertureSize = 3)
img_canny_dilation = cv2.dilate(img_canny, kernel, iterations=3)

## detection
lines = cv2.HoughLinesP(img_canny_dilation, 1, np.pi/180, minLineLength, maxLineGap)

#dilated
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite("hoho.jpg", img)