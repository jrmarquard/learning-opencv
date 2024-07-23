from helpers import download_file
import cv2
import numpy as np

frontalface_file_name = "temp-haarcascade_frontalface_default.xml"
frontalface_src = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"

download_file(frontalface_src, frontalface_file_name)

eye_file_name = "temp-haarcascade_eye.xml"
eye_src = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml"
download_file(eye_src, eye_file_name)

face_cascade = cv2.CascadeClassifier(frontalface_file_name)
eye_cascade = cv2.CascadeClassifier(eye_file_name)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img = cv2.resize(img, None, fx=0.5, fy=0.5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # extremely small and efficient
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.3, 
        minNeighbors=5, 
        # minSize=(30, 30), 
        # flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # region within the face for processing
        roi_gray = gray[y:y+h, x:x+w]
        # region within the face for drawing
        roi_colour = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(
            roi_gray, 
            scaleFactor=1.3, 
            minNeighbors=5
        )
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                roi_colour, 
                (ex, ey), 
                (ex+ew, ey+eh), 
                (0, 255, 0), 
                2
            )
    cv2.imshow('Video', img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:     
        break
    
cap.release()
cv2.destroyAllWindows()
        