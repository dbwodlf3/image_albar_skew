import numpy as np
import cv2

img = cv2.imread("test.jpg")
width, height, chanles = img.shape

print(width)
print(height)

#init

new_img = img[100:][(int(height/2)):-200]

cv2.imshow("good",new_img)
cv2.waitKey(0)

cv2.imwrite("goodMan.jpg", new_img)