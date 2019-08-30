#Imports
from cv2 import cv2
import datetime

#for opening front cam
cap = cv2.VideoCapture(0)

#face detection trained model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#for generating output video file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))


while(True):
    #reading
    ret, frame = cap.read()
    #fliping cam
    frame=cv2.flip(frame,1,0)
    
    #content on screen
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)   
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Width: ' + str(w) + ' Height: '+ str(h)
    datet = str(datetime.datetime.now())
    frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255),1,cv2.LINE_AA)
    frame = cv2.putText(frame,'By Sooraj Kothari',(150,440),font,1,(0,255,0),1,cv2.LINE_AA)
    out.write(frame)
        
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('live face detection',frame)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()


