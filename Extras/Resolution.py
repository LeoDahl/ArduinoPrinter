import os
import cv2
from numpy import asarray
image = cv2.imread('Template.jpg', cv2.IMREAD_GRAYSCALE)

resized_image = cv2.resize(image, (210, 210))
thresh = 127
im_bw = cv2.threshold(resized_image, thresh, 255, cv2.THRESH_BINARY)[1]
numpydata = asarray(im_bw)
cv2.imshow("WAZZAP", im_bw)
print(numpydata)

cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()