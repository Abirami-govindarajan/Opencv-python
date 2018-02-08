import numpy as np
import cv2

image = cv2.imread('C:\Users\classic\Documents\downloaded_img\Jasmine-Flowers.jpg',0)
cv2.imshow("Original_gray",image)

ret, thresh_basic = cv2.threshold(image, 70,255, cv2.THRESH_BINARY)
cv2.imshow('basic_thresh', thresh_basic)

blur = cv2.GaussianBlur(thresh_basic, (5,55),0)
cv2.imshow("Blur",blur)

kernel = np.ones((3,3),'uint8')

dilate = cv2.dilate(thresh_basic,kernel,iterations=1)
erode = cv2.erode(thresh_basic,kernel,iterations=1)

cv2.imshow("Dilate",dilate)
cv2.imshow("Erode",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
