######################################################
#  CREATE BY Thiraphong Thiangphadung                # 
#  เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.          #     
#  lesson6 Cotours                                   #
######################################################
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hands.png')
img1 = img.copy()
img2 = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
hull = cv2.convexHull(cnt)
k=cv2.isContourConvex (hull)

cv2.drawContours(img1, [hull], 0,(0,255,0), 3) # draw line
cv2.drawContours(img2, hull, -1,(0,255,0), 5) # plot points

titles = ['Original','Convex Hull','points']
images = [img, img1, img2]

for i in range(3):
    plt.subplot(1,3,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])
print(k)
plt.show()