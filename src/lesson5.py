# lesson 5
# https://www.youtube.com/watch?v=_gfNpJmWIug&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=5

import cv2
import numpy as np

img1 = cv2.imread('./images/crowd.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('./images/crowd2.jpg', cv2.IMREAD_COLOR)
img3 = cv2.imread('./images/python_logo_white.jpg', cv2.IMREAD_COLOR)


# ADDING EXPERIMENTS
# Add
# add = img1 + img2

# CV2 add
# add = cv2.add(img1, img2)
# this ads the pixel values for each colour channel (max 255 = white)

# CV2 addWeighted
# add = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# cv2.imshow('Img1 + Img2', add)


# SUPERIMPOSING EXPERIMENTS
rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

# mask it
img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 230, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)                    # invert mask
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)  # get bg of img1 where mask is _not_ set
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)    # get fg of img3 where mask _is_ set
dst = cv2.add(img1_bg, img3_fg)                     # paste img3_fg on top of img1_bg
img1[0:rows, 0:cols] = dst                          # overwrite img1 with result

cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('dst', dst)
cv2.imshow('img1 + img3', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
