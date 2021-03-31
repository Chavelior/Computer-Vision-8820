#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:36:35 2021

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

# Divide image into 4 subimages
sub_img1 = image[0:256, 0:256]
sub_img2 = image[256:512, 0:256]
sub_img3 = image[0:256, 256:512]
sub_img4 = image[256:512, 256:512]
#plt.imshow(sub_img3, cmap='gray')

def iterative(image):
    
    # Initial Threshold is the mean
    region1 = []
    region2 = []
    thrshld_init = np.mean(image)
    
    for i in range(0,256,1):
        for j in range(0,256,1):
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
        for i in range(0,256,1):
            for j in range(0,256,1):
                if image[i][j] > thrsh_old:
                    region1.append(image[i][j])
                else:
                    region2.append(image[i][j])
                    
        if(len(region1)!=0):
            mean1_new = math.ceil(np.mean(region1))
        else:
            mean1_new = 0
            
        if(len(region2)!=0):
            mean2_new = math.ceil(np.mean(region2))
        else:
            mean2_new = 0   
        thrsh_new = (mean1_new+mean2_new)/2
        #print(thrsh_new)
        
        if(thrsh_new == thrsh_old):
            break
    
    image_3 = np.copy(image)  
    for i in range(0,256,1):
        for j in range(0,256,1):    
            if image[i][j] > math.ceil(thrsh_new):
                image_3[i][j] = 255
            else:
                image_3[i][j] = 0
    
    return image_3


sub_iter_img1 = iterative(sub_img1)
sub_iter_img2 = iterative(sub_img2)
sub_iter_img3 = iterative(sub_img3)
sub_iter_img4 = iterative(sub_img4)

sub_adapt = np.copy(image)
sub_adapt[0:256, 0:256] = sub_iter_img1
sub_adapt[256:512, 0:256] = sub_iter_img2
sub_adapt[0:256, 256:512] = sub_iter_img3
sub_adapt[256:512, 256:512] = sub_iter_img4

plt.imshow(sub_adapt, cmap='gray')