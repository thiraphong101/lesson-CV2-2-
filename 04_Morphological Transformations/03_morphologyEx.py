###################################################
#  CREATE BY Thiraphong Thiangphadung             # 
#  เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.       #    
#  lesson4 Morphological                          #
###################################################
import cv2
import numpy as np

img = cv2.imread('j.png', 0)
cv2.imshow('j.png', img)
print(img.shape)


kernel = np.ones((5, 5), np.uint8)


opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#cv2.imshow('opening', opening)
#cv2.moveWindow('opening', x=img.shape[1], y=0)


closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#cv2.imshow('closing', closing)
#cv2.moveWindow('closing', x=img.shape[1] * 2, y=0)


gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
#cv2.imshow('gradient', gradient)
#cv2.moveWindow('gradient', x=img.shape[1] * 3, y=0)


tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
#cv2.imshow('tophat', tophat)
#cv2.moveWindow('tophat', x=img.shape[1] * 4, y=0)


blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
#cv2.imshow('blackhat', blackhat)
#cv2.moveWindow('blackhat', x=img.shape[1] * 5, y=0)
cv2.imshow('morphologyEx',np.hstack((img,opening,closing,gradient,tophat,blackhat)))
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
cv2.getStructuringElement()

# Rectangular Kernel
>>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)
# Elliptical Kernel
>>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)
# Cross-shaped Kernel
>>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)
'''
