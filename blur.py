import cv2
ash = cv2.imread('ash.png')

gaussian = cv2.GaussianBlur(ash, (7, 7), 0)
cv2.imshow('ash recorded on an iphone 1', gaussian)

median = cv2.medianBlur(ash, 5)
cv2.imshow('ash recorded on a samsung note 7', median)

bilateral = cv2.bilateralFilter(ash, 9, 75, 75)
cv2.imshow('ash but something', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Gaussian Blur - used mostly in machine learning preprocessing steps
#Gaussian blur describes blurring an image by a Gaussian function. 
#It is a widely used effect in graphics software, typically to reduce image noise and reduce detail.
#(img, Kernal_size ,std_dev)
# Median Blur -widely used in digital image processing because, under certain conditions, 
# it preserves edges while removing noise.
#(img,Kernal_size)
# Bilateral Blur - only sharp edges are preserved here
#(img,diameter of each pixel neighborhood,sigmaColor,sigmaSpace)
