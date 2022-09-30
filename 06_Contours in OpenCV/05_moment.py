######################################################
#  CREATE BY Thiraphong Thiangphadung                # 
#  เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.          #     
#  lesson6 Cotours                                   #
######################################################
import numpy as np
import cv2 as cv
img = cv.imread('test.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
#contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv.moments(cnt)
area_moment = M['m00'] 

print( M )
print( area_moment )


cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
cv.circle(img,(cx,cy), 5, (0,255,255), -1)
print(cx)
print(cy)
area = cv.contourArea(cnt)
perimeter = cv.arcLength(cnt,True)

epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)

k = cv.isContourConvex (cnt)

print("cx =" +str(cx)) #หาจุดศูนย์กลาง แกน x
print("cy =" + str(cy)) #หาจุดศูนย์กลาง แกน y
print("area =" + str(area)) #หาพื้นที่
print("perimeter = " + str(perimeter)) #หาพื้นที่
print("approx = " + str(approx)) #การประมาณรูปร่าง
print("k = " + str(k)) #โค้งนูน

cv.imshow('frame3',img)
cv.waitKey(0)
cv.destroyAllWindows()

