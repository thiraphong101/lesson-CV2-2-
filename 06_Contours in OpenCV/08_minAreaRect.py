######################################################
#  CREATE BY Thiraphong Thiangphadung                # 
#  เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.          #     
#  lesson6 Cotours                                   #
######################################################
import cv2
import numpy as np

img = cv2.imread('blue_thunder.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]
print('len(contours)', len(contours))
cnt = contours[0]

x, y, w, h = cv2.boundingRect (cnt)
cv2.rectangle (img, (x, y), (x + w, y + h), (0,255,0), 2)
cv2.imshow('fd', img)
cv2.waitKey(0)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
cv2.imshow('fd', img)
cv2.waitKey(0)

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(img,center,radius,(255,255,0),2)
cv2.imshow('fd', img)
cv2.waitKey(0)

ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img,ellipse,(255,255,255),2)
cv2.imshow('fd', img)
cv2.waitKey(0)

rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img,(cols-1,righty),(0,lefty),(0,255,255),2)
cv2.imshow('fd', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
