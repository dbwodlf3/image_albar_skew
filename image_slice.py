import cv2
import numpy as np

img = cv2.imread("test.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_smmoth = cv2.GaussianBlur(img_gray, (5,5), cv2.BORDER_DEFAULT)

crop_img = img[0:1000 , 0:1000]

cv2.imwrite("sliced.jpg", img_gray_smmoth)
cv2.imwrite("sliced2.jpg", crop_img)
cv2.waitKey(0)

