import cv2
import numpy as np

def entropy(img):
	hist,_=np.histogram(img)
	hist=hist[hist>0]
	entr=-np.log2(np.float64(hist)/hist.sum()).sum()
	return entr

if __name__=='__main__':
	img=cv2.imread("images/table.png")
	print(entropy(img))