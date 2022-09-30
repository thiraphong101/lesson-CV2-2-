######################################################
#  CREATE BY Thiraphong Thiangphadung                # 
#  เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.          #     
#  lesson6 Cotours                                   #
######################################################
import numpy as np
import cv2
 
img = cv2.imread('test.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(imgray, 0, 25, 0)
#ret, thresh = cv2.threshold(imgray, 0, 100, 0)
#ret, thresh = cv2.threshold(src=imgray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)#src, thresh, maxval, type
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
#img = cv2.drawContours(img, contours, -1, (0,255,0), -1)

cnt = contours[0] #มีรูปร่างเดียว
area = cv2.contourArea(cnt)
print (area)
print(len(contours))
print(len(cnt))
#img = cv2.drawContours(img,[cnt],0,(255,0,0),-1)

cv2.imshow('frame',img)
#cv2.imshow('frame [cnt]',img)
#cv2.imshow('frame -1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()