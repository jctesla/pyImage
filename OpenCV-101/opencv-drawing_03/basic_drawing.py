# USAGE
# python basic_drawing.py

# import the necessary packages
import numpy as np
import cv2
import os

print(f'...Dir Actual = {os.getcwd()}')

# initialize our canvas as a 300x300 pixel image with 3 channels
# (Red, Green, and Blue) with a black background
canvas = np.zeros((300, 300, 3), dtype="uint8")											# color 0 = Black

# draw a green line from the top-left corner to the bottom-right
#        B   G   R-----> RGB
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# save the image (OpenCV handles converting image .bmp <sin comprimir>, jpg <comprimido>, png <comprimidio> etc
cv2.imwrite("Top-Left-Corner.png", canvas)

# draw a 3 pixel thick red line from the top-right corner to the
# bottom-left
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#cv2.imwrite("RedLine_TopRight_Bottom_left.png", canvas)

# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#cv2.imwrite("Square_box50x50_green.png", canvas)

# draw another rectangle, this one red with 5 pixel thickness
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#cv2.imwrite("Rectangle_Red.png", canvas)

# draw a final rectangle (blue and filled in )
#        B   G   R-----> RGB
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#cv2.imwrite("Rctangle_Green_Solid.png", canvas)

# re-initialize our canvas as an empty array, then compute the
# center (x, y)-coordinates of the canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

# loop over increasing radii, from 25 pixels to 150 pixels in 25
# pixel increments
for r in range(0, 175, 25):
	# draw a white circle with the current radius size
	cv2.circle(canvas, (centerX, centerY), r, white)

# show our work of art
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#cv2.imwrite("Circules_inCircules.png", canvas)

# re-initialize our canvas once again
canvas = np.zeros((300, 300, 3), dtype="uint8")

# let's draw 25 random circles
for i in range(0, 25):
	# randomly generate a radius size between 5 and 200, generate a
	# random color, and then pick a random point on our canvas where
	# the circle will be drawn
	radius = np.random.randint(5, high=200)
	color = np.random.randint(0, high=256, size=(3,)).tolist()	# [r,g,b]
	pt = np.random.randint(0, high=300, size=(2,))							# [row,col]

	# draw our random circle on the canvas
	cv2.circle(canvas, tuple(pt), radius, color, -1)

# display our masterpiece to our screen
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#cv2.imwrite("random_25_circles_color.png", canvas)
