import cv2
import numpy as np

img_org = cv2.imread('images/lesson-11-original.jpg')
img_org_gray = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)

# loads it in grayscale
template = cv2.imread('images/lesson-11-template.jpg', 0)
w, h = template.shape[::-1]

# Apply template Matching
res = cv2.matchTemplate(
    img_org_gray, 
    template, 
    cv2.TM_CCOEFF_NORMED
)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    print(f'Match found at {pt}')
    cv2.rectangle(
        img_org,                # Image to draw rectangle on
        pt,                     # Top-left corner of rectangle
        (pt[0] + w, pt[1] + h), # Bottom-right corner of rectangle
        (0, 255, 0),            # Color of rectangle in BGR format
        2                       # Thickness of rectangle
    )
    
cv2.imshow('Detected', img_org)

cv2.waitKey(0)
cv2.destroyAllWindows()
