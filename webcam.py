import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Our operations on the frame come here
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA) # This one is good

    # Display the resulting frame
    cv2.imshow('frame',color)

    # write the flipped frame
    out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('frame', 0) == -1:
    	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()