import cv2
import numpy as np
import matplotlib.pyplot as plt

# cv can read images or videos
img = cv2.imread('../images/crowd.jpg', cv2.IMREAD_GRAYSCALE)

# Show image with CV
# cv2.imshow('Original Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Show image with matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50, 100], [80, 100], 'c', linewidth=5)
# plt.show()
