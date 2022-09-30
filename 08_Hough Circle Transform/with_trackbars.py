#################################################
#  CREATE BY Thiraphong Thiangphadung           # 
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #        
# lesson8 HoughCircles                          #
#################################################
import numpy as np
import cv2 as cv

img = cv.imread('soda.png',0)

def f(x=None):
    return

cv.namedWindow('detected circles', cv.WINDOW_NORMAL)
cv.createTrackbar('Canny Lower', 'detected circles', 100, 255, f)
cv.createTrackbar('Canny Upper', 'detected circles', 200, 255, f)
cv.createTrackbar('Threshold', 'detected circles', 40, 255, f)
cv.createTrackbar('Min Radius', 'detected circles', 0, 255, f)
cv.createTrackbar('Max Radius', 'detected circles', 2, 255, f)
cv.createTrackbar('Min Distance', 'detected circles', 32, 255, f)
cv.createTrackbar('Inverse Resolution', 'detected circles', 1, 10, f)

img = cv.medianBlur(img, 5)

while True:

    canny_lower = cv.getTrackbarPos('Canny Lower', 'detected circles')
    canny_upper = cv.getTrackbarPos('Canny Upper', 'detected circles')
    threshold = cv.getTrackbarPos('Threshold', 'detected circles')
    max_radius = cv.getTrackbarPos('Min Radius', 'detected circles')
    min_radius = cv.getTrackbarPos('Max Radius', 'detected circles')
    min_distance = cv.getTrackbarPos('Min Distance', 'detected circles')
    inverse_resolution = cv.getTrackbarPos('Inverse Resolution', 'detected circles')

    canny = cv.Canny(img, canny_lower, canny_upper)
    cimg = cv.cvtColor(canny,cv.COLOR_GRAY2BGR)

    try:
        circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,
                                  inverse_resolution,
                                  min_distance,
                                  param1=canny_upper,
                                  param2=threshold,
                                  minRadius=min_radius,
                                  maxRadius=max_radius)

        circles = np.uint16(np.around(circles))

        for i in circles[0,:]:
            # draw the outer circle
            cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    except:
        pass

    cv.imshow('detected circles',cimg)

    if cv.waitKey(10) & 0xFF == 27 or cv.waitKey(10) & 0xFF == 'q':
        break


cv.destroyAllWindows()