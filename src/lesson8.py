import cv2
import numpy as np

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
    
    # Trying to find approaches that reduce noise.
    # 1. Simple Average, 2. Gaussian, 3. Median, 4. Bilateral
    
    # kernel = np.ones((15,15), np.float32) / 225
    # smoothed = cv2.filter2D(res, -1, kernel)  # applies simple average of frame
    
    blur = cv2.GaussianBlur(res, (15,15), 0)  # applies Gaussian blur
    median = cv2.medianBlur(res, 15)  # applies median blur
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    cv2.imshow('Original Frame', frame)
    # cv2.imshow('Mask', mask)
    cv2.imshow('Masked Frame', res)
    cv2.imshow('Blur Frame', blur)
    cv2.imshow('Median Frame', median)
    cv2.imshow('Bilateral Frame', bilateral)
    
    # Note: running these all is laggy on my laptop. Consider running only one at a time.

    k = cv2.waitKey(5) & 0xFF
    if k == 27:  # Hold 'ESC' to quit
        break
    
cv2.destroyAllWindows()
cap.release()