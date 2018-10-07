import cv2
import numpy
from pylab import *

def cutRectangle(rec,canvas,ratio):
	return canvas



if __name__=='__main__':
	img=cv2.imread("images/harry.jpeg")
	rect=(150,150,50,50)
	x,y,w,h=rect
	c=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
	img=cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
	#img=cv2.rectangle(img,(x, y), (x+w, y+h), (0, 0, 0), 2)
	cv2.imshow("cutRectangle",img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()