import cv2
import numpy as np

camera1 = cv2.VideoCapture ("video1.avi")
camera2 = cv2.VideoCapture ("video2.avi")
camera3 = cv2.VideoCapture ("video3.avi")
camera4 = cv2.VideoCapture ("video4.avi")

car_cascade = cv2.CascadeClassifier('cars.xml')
while True:
    (grabbed1,frame1) = camera1.read()
    (grabbed2,frame2) = camera2.read()
    (grabbed3,frame3) = camera3.read()
    (grabbed4,frame4) = camera4.read()
    grayvideo1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    grayvideo2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    grayvideo3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
    grayvideo4 = cv2.cvtColor(frame4, cv2.COLOR_BGR2GRAY)
    cars1 = car_cascade.detectMultiScale(grayvideo1, 1.1, 1)
    cars2 = car_cascade.detectMultiScale(grayvideo2, 1.1, 1)
    cars3 = car_cascade.detectMultiScale(grayvideo3, 1.1, 1)
    cars4 = car_cascade.detectMultiScale(grayvideo4, 1.1, 1)
    print("Found {0} cars! in video 1".format(len(cars1 )))
    print("Found {0} cars! in video 2".format(len(cars2 )))
    print("Found {0} cars! in video 3".format(len(cars3 )))
    print("Found {0} cars! in video 4".format(len(cars4 )))
    n1=len(cars1 )
    n2=len(cars2 )
    n3=len(cars3 )
    n4=len(cars4 )
    for (x,y,w,h) in cars1:
       cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
       cv2.imshow("video1",frame1)
    for (x,y,w,h) in cars2:
       cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,0,255),2)
       cv2.imshow("video2",frame2)
    for (x,y,w,h) in cars3:
       cv2.rectangle(frame3,(x,y),(x+w,y+h),(0,0,255),2)
       cv2.imshow("video3",frame3)
    for (x,y,w,h) in cars4:
       cv2.rectangle(frame4,(x,y),(x+w,y+h),(0,0,255),2)
       cv2.imshow("video4",frame4)
    if cv2.waitKey(1)== ord('q'):
       break

camera.release()
cv2.destroyAllWindows()






