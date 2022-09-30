#################################################
#  CREATE BY Thiraphong Thiangphadung           #  
#  เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.     # 
#  lesson7 HoughLines                           #
#################################################
import cv2
import numpy as np

img = cv2.imread("lines.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)

for line in lines:
    print(line[0])
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
#cv2.line(img, (563, 289), (563, 94), (0, 255, 255), 3)
cv2.imshow("Edges", edges)
cv2.imshow("Image", img)
cv2.imwrite("1.3_lines_with_gap.jpg", img)
cv2.imwrite("Edges.jpg", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()