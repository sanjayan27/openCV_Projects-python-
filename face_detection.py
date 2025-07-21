#face detection using haar cascade frontalface algorithm 
import cv2

algorithm = "haarcascade_frontalface_default.xml"

# to load in some variable
haar_cascade = cv2.CascadeClassifier(algorithm)

# initializing camera
camera = cv2.VideoCapture(0)

#use while loop to get the video frames
while True:
    _,image = camera.read() #to read the camera
    
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  #converting normal to grayscale image then only the the model can recognize the face
    
    face_coordinates = haar_cascade.detectMultiScale(gray_image,1.3, 8)  #obtaining face coordinates
    
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(image,(x,y),(x+ w , y + h),(0,255,0),2)
    
    
    cv2.imshow('Face is Detected',image)
    
    key = cv2.waitKey(10)
    if(key == 27):   #27 is the hash code for esc
        break

camera.release()
cv2.destroyAllWindows()