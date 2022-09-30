#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #  
#  lesson3 Perspective                          #
#################################################
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    cv2.circle(frame, (155, 120), 5, (0, 255, 255), -1) #สร้าง จุดวงกลม
    cv2.circle(frame, (480, 120), 5, (0, 0, 255), -1) #สร้าง จุดวงกลม
    cv2.circle(frame, (20, 475), 5, (0, 0, 255), -1) #สร้าง จุดวงกลม
    cv2.circle(frame, (620, 475), 5, (0, 0, 255), -1) #สร้าง จุดวงกลม

    pts1 = np.float32([[155, 120], [480, 120], [20, 475], [620, 475]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (500, 600))


    cv2.imshow("Frame", frame)
    cv2.imshow("Perspective transformation", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()