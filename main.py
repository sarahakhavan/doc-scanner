import cv2
import numpy as np

image = cv2.imread('document.jpg')
orig = image.copy()
image = cv2.resize(image, (800, int(image.shape[0] * 800 / image.shape[1])))





gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 150)

cv2.imshow("Edged", edged)
cv2.waitKey(0)