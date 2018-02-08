import cv2
import numpy as np


img = cv2.imread('C:\Python27\code_image\sun.jpg')
print 'TYPE'
print type(img)
print 'LENGTH'
print len(img)
print 'SHAPE'
print img.shape
print 'DTYPE'
print img.dtype
print 'SIZE'
print img.size
print 'RED CHANNEL'
print img[:,:,0]
print 'GREEN CHANNEL'
print img[:,:,1]
print 'BLUE CHANNEL'
print img[:,:,2]

cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img)
cv2.imwrite('C:\Python27\code_image\photowrite.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
