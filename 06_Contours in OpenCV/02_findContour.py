######################################################
#  CREATE BY Thiraphong Thiangphadung                # 
#  เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.          #     
#  lesson6 Cotours                                   #
######################################################
import numpy as np
import cv2
#im = cv2.imread('contour.jpg')
im = cv2.imread('chessboard.jpeg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

#cv2.imshow("imgray", imgray)


#ret, thresh = cv2.threshold(imgray, 0, 25, 0)
#ret, thresh = cv2.threshold(imgray, 0, 100, 0)
ret, thresh = cv2.threshold(src=imgray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)#src, thresh, maxval, type

#cv2.imshow("thresh", thresh)
#Contour_Retrieval_Mode
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("contours size: ", len(contours))

#img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
img = cv2.drawContours(im, contours, 3, (255, 0, 0), 3)

cnt = contours [7]
cv2.drawContours (im, [cnt], 0, (0,255,0), 3)

cv2.imshow("contour.jpg", im)
cv2.waitKey(0)
