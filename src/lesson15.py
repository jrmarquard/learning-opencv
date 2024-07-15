import cv2
import numpy as np
import requests
import os

# Download the file for this lesson. Prefix temp so git ignores it.
filename = "temp-people-walking.mp4"

def download_file(_filename):
    src = "https://pythonprogramming.net/static/images/opencv/people-walking.mp4"
    # Download file from src and save it as "people-walking.mp4" if it doesn't exist already
    if not os.path.isfile(_filename):
        response = requests.get(src, stream=True)
        if response.status_code == 200:
            with open(_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print(f"File '{_filename}' downloaded successfully.")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
    else:
        print(f"Did not download file. Already exists.")
    

download_file(filename)

cap = cv2.VideoCapture(filename)

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    
    if not ret:
        # Loop back to the start of the video when we reached the end.
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    
    # resize image by 50%
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    
    fgmask = fgbg.apply(frame)

    cv2.imshow('Original', frame)
    cv2.imshow('FG Mask', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:     
        break
    
cap.release()
cv2.destroyAllWindows()
