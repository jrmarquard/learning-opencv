import cv2
import numpy as np
import matplotlib.pyplot as plt

# https://www.youtube.com/watch?v=UquTAf_9dVA
# https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html

img_match = cv2.imread('images/lesson14-pattern-matching-match.jpg', 0)
img_scene = cv2.imread('images/lesson14-pattern-matching-scene.jpg', 0)

# Initiate ORB detector 
# ORB = Oriented Binary Descriptor
# Detect keypoints and compute descriptors.
orb = cv2.ORB_create()

# Keypoints: distinctive local features consistent between scale, rotation, illumination.
# Descriptors: numerical representations of keypoints.
kp1, des1 = orb.detectAndCompute(img_match, None)
kp2, des2 = orb.detectAndCompute(img_scene, None)

# 1st result: list of keypoints detected
# 2nd result: 2d array of descriptors, each corresponds to a keypoint

# Create matcher object. 
# BFMatcher -> Brute Force Matcher
bf = cv2.BFMatcher(
    cv2.NORM_HAMMING, 
    crossCheck=True
)

# Find matching keypoints. 
# The result of matches = bf.match(des1,des2) line is a list of DMatch objects. 
# This DMatch object has following attributes:
#  - DMatch.distance - Distance between descriptors. The lower, the better it is.
#  - DMatch.trainIdx - Index of the descriptor in train descriptors
#  - DMatch.queryIdx - Index of the descriptor in query descriptors
#  - DMatch.imgIdx - Index of the train image.
matches = bf.match(des1, des2)
print(f"{len(matches)} matches found")
print(f"{matches[0].distance:.2f} ")
print(" ".join(str(m.distance) for m in matches[:20]))

# Sort matches by "distance".
# Sort in ascending order of their distances so that 
# best matches (with low distance) come to front. 
matches = sorted(matches, key=lambda x:x.distance)
print(" ".join(str(m.distance) for m in matches[:20]))

img3 = cv2.drawMatches(
    img_match, 
    kp1, 
    img_scene, 
    kp2, 
    matches[:8], 
    None, 
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

plt.imshow(img3)
plt.show()
