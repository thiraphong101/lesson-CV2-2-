######################################################
#  CREATE BY Thiraphong Thiangphadung                # 
#  เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.          #     
#  lesson6 Cotours                                   #
######################################################
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('3.png')
img1 = img.copy()
img2 = img.copy()
img3 = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]


epsilon1 = 0.01*cv2.arcLength(cnt, True)
epsilon2 = 0.1*cv2.arcLength(cnt, True)
epsilon3 = 0.001*cv2.arcLength(cnt, True)

approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
approx2 = cv2.approxPolyDP(cnt, epsilon2, True)
approx3 = cv2.approxPolyDP(cnt, epsilon3, True)

cv2.drawContours(img, [cnt],0,(0,255,0),3) 
cv2.drawContours(img1, [approx1], 0,(0,255,0), 3) # line
cv2.drawContours(img2, [approx2], 0,(0,255,0), 3) # line
cv2.drawContours(img3, approx3, -1, (0, 255, 0), 5)  # points

titles = ['Original', '1%', '10%','points']
images = [img, img1, img2, img3]

for i in range(4):
    plt.subplot(1,4,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()