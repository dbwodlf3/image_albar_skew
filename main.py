import cv2
import numpy as np
import mylib as t

kernel = np.ones((5,5), np.uint8)

img = cv2.imread("test2.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
img_canny = cv2.Canny(img_gray, 50, 200)
img_canny_dilation = cv2.dilate(img_canny, kernel, iterations=3)

cv2.imwrite("zz.jpg", img_canny_dilation)

a = t.getX(img_canny_dilation)

print(a)