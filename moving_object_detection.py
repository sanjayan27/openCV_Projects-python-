import cv2
import imutils

cam = cv2.VideoCapture(0)

firstFrame = None
area = 400

while True:
    text = "normal"
    _,img = cam.read()
    gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    smoothening_img = cv2.GaussianBlur(gray_image,(21,21),0)
    
    
    if firstFrame is None:
        firstFrame = smoothening_img
        continue
    
    imgDiff = cv2.absdiff(firstFrame, smoothening_img)
    
    thresImg = cv2.threshold(imgDiff,40,255,cv2.THRESH_BINARY)[1]
    
    thresImg= cv2.dilate(thresImg,None, iterations= 2)
    
    contours = cv2.findContours(thresImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    grab_contours = imutils.grab_contours(contours)
    
    for contour in grab_contours:
        if(cv2.contourArea(contour) < area):
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        text = "moving object is detected"
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow('gray_imag',img)
    key = cv2.waitKey(10)
    if(key == ord("a")):
        break
    
cam.release()
cv2.destroyAllWindows()