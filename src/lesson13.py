import cv2
import numpy as np

img = cv2.imread('images/crowd.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray) # converts to float32 for the algorithm we will use

corners = cv2.goodFeaturesToTrack(
    gray, 
    50,     # Find 50 of them
    0.1,    # Image quality
    5       # minimum distance between corners
)
corners = np.int0(corners)

for corner in corners:
    # Get coordinates
    x, y = corner.ravel()   
    # Draw the corner on the image
    # Circle with radius 3, color red, filled
    cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
    
cv2.imshow('Corners', img)
# Note on result
# Finds corners all over the place since the image
# is a photograph of a crowd.

cv2.waitKey(0)
cv2.destroyAllWindows()