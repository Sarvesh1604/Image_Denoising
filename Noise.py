import cv2

img = cv2.imread('image.jpg',1)
m, n = img.shape[:2]

#Selecting random pixels and changing their value
import random
img_copy = img
t = int(0.04*m*n)                 #taking 4% of the total pixels
for i in range(0,t):
  index1 = random.randint(0,m-1)
  index2 = random.randint(0,n-1)
  img_copy[index1][index2] = random.sample(range(1,255), 3)

#Displaying and saving the image with added noise
cv2.imwrite('with_noise.jpg', img_copy)