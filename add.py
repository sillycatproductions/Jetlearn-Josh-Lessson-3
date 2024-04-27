import cv2
ash = cv2.imread('ash.png')
pikachu = cv2.imread('pikachu.png')

# 0.5 and 0.4 is the opacity of each image when you add/combine them and 0 is the light measurement
weightedSum = cv2.addWeighted(ash,0.5,pikachu,0.4, 0)

cv2.imshow('Wighted Image', weightedSum)

cv2.waitKey(0)
cv2.destroyAllWindows()