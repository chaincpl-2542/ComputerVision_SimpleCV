import cv2 as cv
import numpy as np

imageKoiking = cv.imread("Koiking.png")
imageGyarados = cv.imread("Gyarados.png")

gray_image_Koiking = cv.cvtColor(imageKoiking, cv.COLOR_BGR2GRAY)
gray_image_Gyarados = cv.cvtColor(imageGyarados, cv.COLOR_BGR2GRAY)

circle_image_Koiking = gray_image_Koiking.copy()
width, height = circle_image_Koiking.shape[:2]
circle_Redius = 40
cv.circle(circle_image_Koiking, (width - circle_Redius, height - circle_Redius), circle_Redius, 0, -1)

combined_image_left = np.vstack((circle_image_Koiking, gray_image_Gyarados))
combined_image_right = np.vstack((gray_image_Koiking, gray_image_Gyarados))

ret, binary_combined_image_right = cv.threshold(combined_image_right,127,255,cv.THRESH_BINARY)

combined_image = np.hstack((combined_image_left, binary_combined_image_right))

cv.imshow("Koiking",combined_image)
cv.waitKey(0)
