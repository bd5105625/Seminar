import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import cm
from cv2 import cv2 as cv
import argparse
import imutils


def Segmentation(rootpath , img , jpgimage):
    jpgpath = rootpath + "/" + jpgimage
    # print(path , jpgpath)
    # img = cv.imread(path , 0)
    # blurred = cv.GaussianBlur(img, (11, 11), 0)#高斯模糊化
    canny = cv.Canny(img , 30 , 150)#threshold_one and threshold_two
    # canny = cv.Canny(img , 30 , 150)
    canny = cv.dilate(canny , None)
    canny = cv.erode(canny , None)

    #Parameter 
    BLUR = 21
    MASK_DILATE_ITER = 10
    MASK_ERODE_ITER = 10
    MASK_COLOR = (0.0 , 0.0 , 0.0) #In RGB format

    contour_info = []
    contours,_ = cv.findContours(canny , cv.RETR_EXTERNAL , cv.CHAIN_APPROX_SIMPLE)
    for c in contours:
        contour_info.append((
            c,
            cv.isContourConvex(c),
            cv.contourArea(c),
        ))

    contour_info = sorted(contour_info , key = lambda c: c[2] , reverse = True)
    #create empty mask, draw filled polygon on its corresponding to largest contour
    #Mask is black, polygon is white
    mask = np.zeros(canny.shape)

    max_contour = contour_info[0]
    cv.fillConvexPoly(mask , max_contour[0] , (255))
    max_contour = contour_info[1]
    cv.fillConvexPoly(mask , max_contour[0] , (255))

    plt.imshow(mask)
    #smooth mask then blur it
    mask = cv.dilate(mask , None , iterations = MASK_DILATE_ITER)
    mask = cv.erode(mask , None , iterations = MASK_ERODE_ITER)
    mask = cv.GaussianBlur(mask , (BLUR , BLUR) , 0)

    org = cv.imread(jpgpath , 0)
    for i in range(0,512):
        for j in range(0,512):
            if mask[i,j] <= 200:
                org[i,j] = 0
                
    # cv.imwrite(rootpath + "/Segmentation/" + jpgimage , org)
    seg_path = rootpath + "/Segmentation/"
    if not os.path.isdir(seg_path):
        os.mkdir(seg_path)
    cv.imwrite(seg_path + jpgimage + ".jpg" , org)
    # cv.imwrite("mask.jpg" , mask)

def GrayScale(path , filelist):
    # print(len(filelist))
    thresh = []
    for file in filelist:
        print(path + "/" + file)
        img = cv.imread(path + "/" + file)
        _,thresh = cv.threshold(img,160,255,cv.THRESH_BINARY)
        # thresh.append(temp)
        # cv.imwrite(str(i)+".jpg" , thresh[i])
    # for i in range(len(thresh)):
    #     cv.imwrite(str(i)+".jpg" , thresh[i])
        Segmentation(path , thresh , file)

if __name__ == '__main__':
    path = "test/"
    filelist = []
    filename = r".jpg"
    for item in os.listdir(path):
        if item.endswith(filename):
            print(item)
            filelist.append(item)
    print(filelist[0:3])
    GrayScale(path , filelist)
