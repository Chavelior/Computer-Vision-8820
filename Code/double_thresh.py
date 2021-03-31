#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:19:43 2021

@author: akhila
"""

import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt
import math

# Double Thresholding
image = cv2.imread('test3.png', 0)
image = cv2.medianBlur(image,5)

# Extract histogram values
hist = cv2.calcHist([image],[0],None,[256],[0,256])
#plt.hist(image.ravel(),256,[0,256]); plt.show()

# Initial thresholds are at center of first and second halves
thresh_1 = math.ceil(127/2)
thresh_2 = math.ceil((127+256)/2)

reg_1 = np.zeros((512,512),dtype='uint8')
reg_2 = np.zeros((512,512),dtype='uint8')
reg_3 = np.zeros((512,512),dtype='uint8')

for x in range(0,512,1):
    for y in range(0,512,1):
        if image[x][y] < thresh_1:
            reg_1[x][y] = image[x][y]
            #if image[x][y] == 0 : reg_1[x][y] = 1
        else:
            if image[x][y] >= thresh_1 and image[x][y] <= thresh_2:
                reg_2[x][y] = image[x][y]
            else:
                if image[x][y] > thresh_2:
                    reg_3[x][y] = image[x][y]

                    
# Visit each pixel of R2, if it has a neighbour in R1, mark it as R1
count = 1
itera = 0

reg_22 = np.copy(reg_2)
while count!=0:
    count=0
    for x in range(0,512,1):
        for y in range(0,512,1):
            #print(x,y)
            if reg_2[x][y] != 0:
                if (x-1) >= 0 and (y-1) >= 0 and (x+1) <= 511 and (y+1) <= 511:
                    if (reg_1[x][y-1] != 0) and (reg_1[x+1][y] != 0) and (reg_1[x-1][y] != 0) and (reg_1[x][y+1] != 0):
                        #print(x,y,reg_2[x][y],reg_1[x][y-1],reg_1[x+1][y],reg_1[x-1][y], reg_1[x][y+1])
                        reg_2[x][y] = 0
                        reg_1[x][y] = image[x][y]
                        count += 1
                        itera += 1
          
                           
# For every non-assgned R2, assign it to R3
for x in range(0,512,1):
    for y in range(0,512,1):
        if reg_2[x][y] != 0:
            reg_3[x][y] = image[x][y]
            reg_2[x][y] = 0
            
for x in range(0,512,1):
    for y in range(0,512,1):
        if reg_1[x][y] != 0:
            reg_1[x][y] = 255
        else:
            reg_1[x][y] = 0
            
plt.imshow(reg_1, cmap='gray')