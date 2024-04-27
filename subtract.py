import cv2
ash = cv2.imread('ash.png')
pikachu = cv2.imread('pikachu.png')

#subtracts the pixel count from pikachu and ash 
subtract = cv2.subtract(ash,pikachu)
soup = cv2.resize(subtract,(2048,1024))
cv2.imshow('PIKACHU DEMON', soup)

cv2.waitKey(0)
cv2.destroyAllWindows()