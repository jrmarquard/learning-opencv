import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0 = default camera (webcam)
# cv2.namedWindow("Display", cv2.WINDOW_AUTOSIZE) 

# display original frame and laplacian side by side in one window
# ditching this because there's a but when concatenating images
def display4Frames(name1, frame1, name2, frame2, name3, frame3, name4, frame4):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame1, name1, (10, 100), font, 3, (255, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(frame2, name2, (10, 100), font, 3, (255, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(frame3, name3, (10, 100), font, 3, (255, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(frame4, name4, (10, 100), font, 3, (255, 255, 255), 4, cv2.LINE_AA)

    cv2.imshow(
        "Display", 
        np.concatenate(
            (
                np.concatenate((frame1, frame2), axis=1),
                np.concatenate((frame3, frame4), axis=1)
            ), 
            axis=0)
        )

while True:
    _, frame = cap.read()
    
    # reduce frame size by 30%
    frame = cv2.resize(frame, (0, 0), fx=0.3, fy=0.3)
    
    # used for edge detection
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 100, 200)
    
    def displayFrame (i, text):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(i, text, (10, 100), font, 3, (0, 0, 0), 7, cv2.LINE_AA) # border
        cv2.putText(i, text, (10, 100), font, 3, (255, 255, 255), 4, cv2.LINE_AA) # white text
        cv2.imshow(f"{text} Frame", i)
    
    displayFrame(frame, "Original")
    displayFrame(laplacian, "Laplacian")
    displayFrame(sobelx, "sobel x")
    displayFrame(sobely, "sobel y")
    displayFrame(edges, "edges")
    
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # Hold 'ESC' to quit
        break
    
cv2.destroyAllWindows()
cap.release()