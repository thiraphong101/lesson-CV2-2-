##################################################
#  CREATE BY Thiraphong Thiangphadung            #  
#  เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #     
#  lesson5 canny                                 #
##################################################
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)
edges = cv2.Canny(img, 50, 200) # img,minValและmaxVal 

cv2.imshow('Edges',edges)
cv2.waitKey(0)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
