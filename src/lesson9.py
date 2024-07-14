import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0 = default camera (webcam)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_colour = np.array([50, 10, 0])
    upper_colour = np.array([100, 240, 255])

    # HSV --> Hue, Saturation, Value
    mask = cv2.inRange(hsv, lower_colour, upper_colour)
    res = cv2.bitwise_and(frame, frame, mask=mask)  # applies the mask to the frame
    
    # 2 types of morphological transformations: erosion and dilation
    
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)
    
    # opening: removes false-positives
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    # closing: removes false-negatives
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    # Write text onto top left corner of the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Press 'ESC' to quit", (10, 20), font, 3, (255, 255, 255), 1, cv2.LINE_AA)
    
    # not coded, but look at tophat and blackhat for more advanced operations
    # Tophat: difference between original and opening
    # Blackhat: difference between original and closing
    
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Masked Frame', res)
    
    cv2.putText(erosion, "Erosion", (10, 100), font, 3, (255, 255, 255), 4, cv2.LINE_AA)
    cv2.imshow('Erosion Frame', erosion)
    cv2.putText(dilation, "Dilation", (10, 100), font, 3, (255, 255, 255), 4, cv2.LINE_AA)
    cv2.imshow('Dilation Frame', dilation)
    cv2.putText(opening, "Opening", (10, 100), font, 3, (255, 255, 255), 4, cv2.LINE_AA)
    cv2.imshow('opening', opening)
    cv2.putText(closing, "Closing", (10, 100), font, 3, (255, 255, 255), 4, cv2.LINE_AA)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # Hold 'ESC' to quit
        break
    
cv2.destroyAllWindows()
cap.release()