import numpy as np
import cv2

img = cv2.imread('./images/crowd.jpg', cv2.IMREAD_COLOR)

# often will convert to grayscale for simpler processing

# colour value at this pixel
px = img[55,55]
print(px)
# modify pixel value
img[55,55] = [255, 255, 0]

# ROI = Region of Image
roi = img[100:150, 100:150] # <-- all the pixel values in this region
# make it white
img[100:150, 100:150] = [255, 255, 255]

# can copy sections using ROI
roi_1 = img[300:400, 100:200]
img[400:500, 200:300] = roi_1

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
