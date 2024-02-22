import time
import cv2
import matplotlib.pyplot as plt
import numpy as np
#
img_china = cv2.imread('china.jpg')
# img_cat = cv2.imread('cat.jpg') # inform:BGR
# # cv2.IMREAD_GRAYSCALE : 0
# img_cat_gray = cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)
def cv_show(img): # show image
    cv2.imshow("Picture",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cv_show_vedio(name,name2):
    vc = cv2.VideoCapture(name) # get frame from Vedio
    if vc.isOpened(): # bool
        open,frame = vc.read() # bool(to show is other frame excite) + real_frame(to be read)
    else:
        open = False

    while open:
        ret,frame = vc.read()
        if frame is None:
            break
        if ret == True:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY) # cv2.COLOR_BGRA2GRAY : 10
            cv2.imshow(name2,gray)
            if cv2.waitKey(5) & 0xFF == 32:
                break
    vc.release()
    cv2.destroyAllWindows()

def proportional_scaling(name,img,SCALE):
    rows,cols = img.shape[:2]
    new_cols = int(cols*SCALE)
    new_rows = int(rows*SCALE)

    scale_percent = (new_cols,new_rows)
    img_resized =cv2.resize(img,scale_percent,interpolation=cv2.INTER_AREA) #面积插值
    return  img_resized

# image_size=img_china.shape
#
# img_cat_resize=cv2.resize(img_cat,(image_size[1],image_size[0])) # width height
# # cv_show("resize",img_cat_resize)
# weighted=0.7
# img_catAddchina=cv2.addWeighted(img_cat_resize,weighted,img_china,1-weighted,0)
# cv_show(img_catAddchina)

#cv_show_vedio("landspace.mp4","landspace")

# data = open(f"./img_data.txt",'w',encoding="utf-8")
# data.write("BGR Matrix :\n")
# data.write(str(img))
# data.write("\n")
# data.write("Gray Matrix :\n")
# data.write(str(img_gray))
# data.close()

# cv_show(img_china)
# cv_show("imag_gray",img_gray)

#This is an useless sentence, to test the Branch Operate，and this sentence is from the remote repository!
