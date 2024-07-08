# https://www.youtube.com/watch?v=Jvf5y21ZqtQ&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=2

# video feed we need cv2
import cv2
import numpy as np

# 0 = First video capture in system.
cap = cv2.VideoCapture(0)

# Get the width and height of the frame - necessary for VideoWriter to save correctly.
ret, frame = cap.read()
height, width = frame.shape[:2]

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('out/lesson2_output.avi', fourcc, 20.0, (width, height))

while True:
    # true/false, actual frame
    ret, frame = cap.read()
    
    # Write the frame to the output video file
    out.write(frame)
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Video Feed - Original', frame)
    cv2.imshow('Video Feed - Gray', gray)

    # Close the window when 'q' is pressed
    # waitKey() returns 32-bit int. &0xFF masks the last byte so we 
    # can compare with ASCII value of 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Q Pressed. Stopping Video.')
        break

    # Break the loop if the end of the video is reached or an error occurs
    if not ret:
        print('End of Video. Stopping Video.')
        break

# Release the video capture object
cap.release()
out.release() # Release the VideoWriter object
cv2.destroyAllWindows()