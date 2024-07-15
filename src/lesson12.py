import cv2
import numpy as np
import matplotlib.pyplot as plt

# manual version of fg extraction

img = cv2.imread('images/crowd.jpg')
mask = np.zeros(img.shape[:2], dtype=np.uint8)

# bdgModel, fgdModel - These are arrays used by the 
# algorithm internally. You just create two np.float64 
# type zero arrays of size (1,65).
bgdModel = np.zeros((1, 65), dtype=np.float64)
fgdModel = np.zeros((1, 65), dtype=np.float64)

# (x,y,w,h)
rect = (120, 350, 200, 200)
# works well enough for education : )

# Extract objects from images, effectively separating the 
# foreground (object of interest) from the background.
# Read more: https://docs.opencv.org/3.4/d8/d83/tutorial_py_grabcut.html
cv2.grabCut(
    img, 
    mask, 
    rect,                   # rectangle containing foreground object
    bgdModel,
    fgdModel, 
    5,                      # number of iterations
    cv2.GC_INIT_WITH_RECT   # use rectangle initialization
)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype(np.uint8)
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()