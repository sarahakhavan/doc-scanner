import cv2
import numpy as np

img = cv2.imread("D1.jpg")
cv2.imshow("Test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()