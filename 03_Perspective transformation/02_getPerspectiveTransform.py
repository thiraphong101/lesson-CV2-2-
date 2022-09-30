#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #  
#  lesson3 Perspective                          #
#################################################
'''
3x3 
cv2.getPerspectiveTransform()
cv2.warpPerspective 3x3 transformation 

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sudoku.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

cv2.circle(img,(56, 65), 5, (0,255,0), -1)
cv2.circle(img,(368, 52), 5, (0,255,0), -1)
cv2.circle(img,(28, 387), 5, (0,255,0), -1)
cv2.circle(img,(389, 390), 5, (0,255,0), -1)
cv2.putText(img,'p1',(56,65),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,255),2) 
cv2.putText(img,'p2',(368,52),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,255),2) 
cv2.putText(img,'p3',(28,387),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,255),2) 
cv2.putText(img,'p4',(389,390),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,255),2) 

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()