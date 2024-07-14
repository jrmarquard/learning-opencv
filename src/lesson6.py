import cv2
import numpy as np

img = cv2.imread('./images/bookpage.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

# adaptive threshold = applying it on smaller regions of the image
#  - ADAPTIVE_THRESH_GAUSSIAN_C = the threshold value is calculated as the 
#    weighted sum of the neighboring pixels using a Gaussian window.
# - cv2.THRESH_BINARY indicates that the pixels will be set to 
#   either 0 or maxValue based on whether they exceed the threshold.
# - 115 is the size of the Gaussian kernel ("window")
# - 1 is the constant subtracted from the mean calculated for each pixel. 
#   Used to fine tune. The C parameter can be adjusted to control the 
#   sensitivity of the adaptive thresholding. A larger value for C will 
#   result in a higher threshold value, making the thresholded image more 
#   selective (i.e., more pixels will be set to 0). Conversely, a smaller 
#   value for C will result in a lower threshold value, making the thresholded 
#   image less selective (i.e., more pixels will be set to maxValue).
gaus = cv2.adaptiveThreshold(
    grayscaled, 
    255, 
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    cv2.THRESH_BINARY,
    115,
    1 )


# otsu's thresholding is another method for finding the optimal threshold value.
# not ideal for this image.
retval3, otsu_threshold = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold - gray', grayscaled)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu_threshold', otsu_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()