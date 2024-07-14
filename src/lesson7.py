import cv2
import numpy as np

# This tut implements a technique similar to green screening.

cap = cv2.VideoCapture(0) # 0 = default camera (webcam)

while True:
    _, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # converts to hsv colours
    # Want to use this for range purposes. Easier to do this with HSV rather than RGB.
    lower_colour = np.array([50, 10, 0])  # lower limit
    upper_colour = np.array([100, 240, 255])  # upper limit

    # HSV --> Hue, Saturation, Value
    mask = cv2.inRange(hsv, lower_colour, upper_colour)
    res = cv2.bitwise_and(frame, frame, mask=mask)  # applies the mask to the frame

    cv2.imshow('Original Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Masked Frame', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:  # Hold 'ESC' to quit
        break
    
cv2.destroyAllWindows()
cap.release()