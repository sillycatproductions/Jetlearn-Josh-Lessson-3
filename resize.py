import cv2
ash = cv2.imread('ash.png')
cv2.imshow('Ash', ash)

#resizes the image

bigash = cv2.resize(ash,(2048,1024))
cv2.imshow('BIG ASH',bigash)
smolash = cv2.resize(ash,(50,50))
cv2.imshow('smol ash', smolash)

cv2.waitKey(0)
cv2.destroyAllWindows()