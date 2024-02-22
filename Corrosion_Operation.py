import time
import cv2
import matplotlib.pyplot as plt
import numpy as np
import Basic_Image_Processing as bip # Basic Image Processing

img_jimmy =cv2.imread("jimmy.jpg",cv2.IMREAD_GRAYSCALE)
img_jimmy_resized = bip.proportional_scaling("Picture",img_jimmy,0.3)

# kernel=np.ones((5,5),np.uint8)
# dilate=cv2.dilate(img_jimmy_resized,kernel,iterations=4)
# erosion=cv2.erode(img_jimmy_resized,kernel,iterations=4)
#
# res =np.hstack((dilate,erosion))
# bip.cv_show(res)

# gradient=cv2.morphologyEx(img_jimmy_resized,cv2.MORPH_BLACKHATb ,kernel,iterations=1)
# bip.cv_show(gradient)

sobelx=cv2.Sobel(img_jimmy_resized,cv2.CV_64F,1,0,ksize=3) # cv2.CV_64F : 6
sobely =cv2.Sobel(img_jimmy_resized,cv2.CV_64F,0,1,ksize=3)
sobely =cv2.convertScaleAbs(sobely)
sobelx=cv2.convertScaleAbs(sobelx)
sobel=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
#bip.cv_show(sobel)

scharrx = cv2.Scharr(img_jimmy_resized,cv2.CV_64F,1,0)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.Scharr(img_jimmy_resized,cv2.CV_64F,0,1)
scharry=cv2.convertScaleAbs(scharry)
scharr=cv2.addWeighted(scharrx,0.5,scharry,0.5,0)
#bip.cv_show(scharrx)

laplacian=cv2.Laplacian(img_jimmy_resized,cv2.CV_64F)
#bip.cv_show(laplacian)

result = np.hstack((sobel,scharr,laplacian))
#bip.cv_show(result)