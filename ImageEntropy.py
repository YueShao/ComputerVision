import cv2
import numpy as np

def entropy(img):
	hist,_=np.histogram(img)
	hist=hist[hist>0]
	p=np.float64(hist)/hist.sum()
	entr=-(p*np.log2(p)).sum()
	return entr

if __name__=='__main__':
	img=cv2.imread("images/tableContrastEnhance.jpg",0)
	print(entropy(img))