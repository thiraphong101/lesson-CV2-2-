#################################################
#  CREATE BY Thiraphong Thiangphadung           # 
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #   
# lesson1 Changing Color-space                  #
#################################################
import cv2
import numpy as np
#lower_red = np.array([131,92,141]) #red
#upper_red = np.array([179,255,255])

#lower_green = np.array([50,38,169]) #green
#upper_green = np.array([82,255,255])

#lower_yellow = np.array([18,32,214]) #yellow
#upper_yellow = np.array([31,255,255])

lower_blue = np.array([91,93,199]) #blue
upper_blue = np.array([105,255,255])

#lower_orange = np.array([10,67,232]) #orange
#upper_orange = np.array([29,255,255])

#lower_violet = np.array([110,70,171]) #violet
#upper_violet = np.array([121,255,255])
cap = cv2.VideoCapture(0) # รับวิดีโอจากกล้อง
while(1):
	# รับข้อมูลจากเว็บแคม
	ret, frame = cap.read()
	# แปลงสี BGR ไปยัง HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# ช่วงของสีเหลืองในระบบ HSV
	lower_blue = np.array([75,50,50], dtype=np.uint8)
	upper_blue = np.array([130,255,255], dtype=np.uint8)
	# จำกัดภาพ HSV รับเฉพาะสีเหลิอง
	blue = cv2.inRange(hsv, lower_blue, upper_blue)
	# Bitwise-AND mask และภาพต้นฉบับ
	mask = cv2.bitwise_and(frame,frame, mask= blue)

	cv2.imshow('frame',frame)
	cv2.imshow('blue',blue)
	cv2.imshow('mask',mask)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
cv2.destroyAllWindows()
