import numpy as np
import cv2

color = cv2.imread('C:\Python27\code_image\Jasmine-Flowers.jpg',1)

gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite('C:\Python27\code_image\Jasmine-Flowers_gray.jpg',gray)

b,g,r = cv2.split(color)

rgba = cv2.merge((b,g,r,g))
cv2.imwrite('C:\Python27\code_image\Jasmine-Flowers_rgba.png',rgba)
