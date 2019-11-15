import numpy as np
import cv2
import rotate as t

kernel = np.ones((5,5), np.uint8)

img = t.getRotation(cv2.imread("test2.png"))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
img_canny = cv2.Canny(img_gray, 50, 200)
img_canny_dilation = cv2.dilate(img_canny, kernel, iterations=3)

a = cv2.cornerHarris(img_canny_dilation, 2, 3, 0.04)

a = cv2.dilate(a, None, iterations=6)

img[a>0.01*a.max()] = [255, 0, 0]

cv2.imwrite("gg.png", img)