import numpy as np
import cv2 as cv
im = cv.imread('bacteria_left_32_color.jpg')
assert im is not None, "file could not be read, check with os.path.exists()"
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
_, thresholded = cv.threshold(imgray, 127, 255, cv.THRESH_BINARY)
# ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, _ = cv.findContours(thresholded, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(len(contours))