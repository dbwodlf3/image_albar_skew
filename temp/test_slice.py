import cv2
import numpy as np

img = cv2.imread("test2.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_result = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_gray = np.float32(img_gray)
result = cv2.cornerHarris(img_gray, 2, 3, 0.04)
result = cv2.dilate(result, None, iterations=6)

img_result[result>0.01*result.max()] =[255, 0, 0]

cv2.imwrite("img_result.jpg",img_result)