import cv2
import numpy as np

ash = cv2.imread('ash.png')
kernel = np.ones((4,4), np.uint8)
print(kernel)

#]kernel is used to erode the image
#uint8 unsigns integer of 8 bit
ashh = cv2.erode(ash, kernel)
cv2.imshow('Ash drawing', ashh)

cv2.waitKey(0)
cv2.destroyAllWindows()