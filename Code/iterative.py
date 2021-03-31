#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:58:19 2021

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

# Initial Threshold is the mean
region1 = []
region2 = []
thrshld_init = np.mean(image)

for i in range(0,512,1):
    for j in range(0,512,1):
        if image[i][j] > thrshld_init:
            region1.append(image[i][j])
        else:
            region2.append(image[i][j])
            
mean1 = math.ceil(np.mean(region1)) 
mean2 = math.ceil(np.mean(region2))
thrsh_new = math.ceil(mean1+mean2)
# Partition the image into 2 groups

while True : 
    region1 = []
    region2 = []
    thrsh_old = thrsh_new
    #print('thrsh_old')
    for i in range(0,256,1):
        for j in range(0,256,1):
            if image[i][j] > thrsh_old:
                #print('great')
                region1.append(image[i][j])
            else:
                #print('low')
                region2.append(image[i][j])
    if(len(region1)!=0) : 
        print('rowdy')
        mean1_new = math.ceil(np.mean(region1))
    else:
        mean1_new = 0
    mean2_new = math.ceil(np.mean(region2))
    thrsh_new = (mean1_new+mean2_new)/2
    print(thrsh_new)
    
    if(thrsh_new == thrsh_old):
        break

image_3 = np.copy(image)  
for i in range(0,512,1):
    for j in range(0,512,1):    
        if image[i][j] > math.ceil(thrsh_new):
            image_3[i][j] = 255
        else:
            image_3[i][j] = 0

plt.imshow(image_3, cmap='gray')