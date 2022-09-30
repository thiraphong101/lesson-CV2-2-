#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #  
#  lesson3 Perspective                          #
#################################################
import cv2
import numpy as np

img = cv2.imread("book.jpg", cv2.IMREAD_UNCHANGED)
#img = cv2.resize(ori_img,(0,0),fx=0.50,fy=0.50)
print(img.shape)
cv2.circle(img, (200, 40), 5, (0, 0, 255), -1)
cv2.circle(img, (550, 40), 5, (0, 0, 255), -1)
cv2.circle(img, (120, 400), 5, (0, 0, 255), -1)
cv2.circle(img, (630, 400), 5, (0, 0, 255), -1)
pst_1=[200,40]
pst_2=[550,40]
pst_3=[120,400]
pst_4=[630,400]
print(pst_1[0])
pts1 = np.float32([pst_1, pst_2, pst_3, pst_4])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img, matrix, (500, 600))
"""
cv2.circle(img, (235, 103), 5, (0, 0, 255), -1)
cv2.circle(img, (740, 100), 5, (0, 0, 255), -1)
cv2.circle(img, (16, 561), 5, (0, 0, 255), -1)
cv2.circle(img, (990, 562), 5, (0, 0, 255), -1)

pts1 = np.float32([[235, 103], [740, 100], [16, 561], [990, 562]])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img, matrix, (500, 600))
"""


cv2.imshow("Img", img)
cv2.imshow("Perspective transformation", result)
#cv2.imwrite("perspective_transformed.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()