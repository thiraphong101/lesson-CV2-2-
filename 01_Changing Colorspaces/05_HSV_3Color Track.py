#################################################
#  CREATE BY Thiraphong Thiangphadung           # 
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #   
# lesson1 Changing Color-space                  #
#################################################
#importing modules
import cv2   
import numpy as np

#capturing video through webcam
webcam = cv2.VideoCapture(0)
picred = 0
while(webcam.isOpened()):

    ret, img = webcam.read()
    if ret:
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #definig the range of red color
        red_lower=np.array([136,87,111],np.uint8)
        red_upper=np.array([180,255,255],np.uint8)

    #defining the Range of Blue color
        blue_lower=np.array([99,115,150],np.uint8)
        blue_upper=np.array([110,255,255],np.uint8)

    #defining the Range of yellow color
        yellow_lower=np.array([22,60,200],np.uint8)
        yellow_upper=np.array([60,255,255],np.uint8)

    #finding the range  of red,blue and yellow color in the image
        red=cv2.inRange(hsv, red_lower, red_upper)
        blue=cv2.inRange(hsv,blue_lower,blue_upper)
        yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)

    #Morphological transformation, Dilation     
        kernal = np.ones((5 ,5), "uint8")

        red=cv2.dilate(red, kernal)
        res=cv2.bitwise_and(img, img, mask = red)

        blue=cv2.dilate(blue,kernal)
        res1=cv2.bitwise_and(img, img, mask = blue)

        yellow=cv2.dilate(yellow,kernal)
        res2=cv2.bitwise_and(img, img, mask = yellow)    

        #print(img.shape)
        cv2.rectangle(img,(200,img.shape[0]-100),(img.shape[1],img.shape[0]),(255,255,255),3)
        cv2.rectangle(img,(200,img.shape[0]-100),(img.shape[1],img.shape[0]),(255,255,255),-1)

        cv2.putText(img,"RED "+str(picred),(200,img.shape[0]-80),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

       #Tracking the Red Color
        (contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE[, contours[, hierarchy[, offset]]])
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>200):
                x,y,w,h = cv2.boundingRect(contour) 
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
                cv2.putText(img,"RED "+str(pic+1),(x,y-20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
                picred = pic+1


    #Tracking the Blue Color
        (contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>200):
                x,y,w,h = cv2.boundingRect(contour) 
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

    #Tracking the yellow Color
        (contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>200):
                x,y,w,h = cv2.boundingRect(contour) 
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(img,"yellow  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))  



        #cv2.imshow("Redcolour",red)
        cv2.imshow("Color Tracking",img)
        #cv2.imshow("red",res)  
        if cv2.waitKey(10) & 0xFF == ord('q'):
                break 
webcam.release()
cv2.destroyAllWindows()
