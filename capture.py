import cv2, time

video-cv2.VideoCapture(0)
a=0
while True:
    a=a+1
    check, frame = video.read()
    
    print (check)
    print(frame)
    
    cv2.imshow("capturing", frame)
    
    cv2.waitKey(1)
    if key==ord('e'):
        break
print(a)
video.release()