import cv2 as cv
import sys

image_path = "./123.png"

img = cv.imread(image_path)

if img is None:
    sys.exit("Could not read the image.")

gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

edges = cv.Canny(img,100,200, L2gradient = True)


cv.imshow("Display window", img)
cv.imshow("Edges", edges)

cv.waitKey(0)
cv.destroyAllWindows()