######################################################
#  CREATE BY Thiraphong Thiangphadung                # 
#  เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.          #     
#  lesson6 Cotours                                   #
######################################################
import cv2
import numpy as np
img = cv2.imread('balls.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 3)
for h,cnt in enumerate(contours):
	area = cv2.contourArea(cnt)
	if area > 500:
		mask = np.zeros(imgray.shape,np.uint8)
		cv2.drawContours(mask,[cnt],0,255,-1)
		mean = cv2.mean(img,mask = mask)
		print(mean)
		cv2.imshow('frame',mask)
		cv2.waitKey(0)
cv2.destroyAllWindows()