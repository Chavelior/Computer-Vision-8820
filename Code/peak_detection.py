
import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt
import math

# Double Thresholding
image = cv2.imread('test1.png', 0)
image = cv2.medianBlur(image,5)

# Extract histogram values
hist = cv2.calcHist([image],[0],None,[256],[0,256])
plt.hist(image.ravel(),256,[0,256]); plt.ylim(0,2500) ;plt.show()


# Peaks selection 
# The highest threshold selected is 2000
peaks = []
peaks_indx = []
for count, item in enumerate(hist):
    if item >= 2000 : 
        peaks.append(item) 
        peaks_indx.append(count)
# 18 peaks detected

# Valley selection
# Minimum value threshold selected is 400
valleys = []
valleys_indx = []
for count,item in enumerate(hist):
    if item < 400 : 
        valleys.append(item)
        valleys_indx.append(count)
# 41 valleys detected
        
# Initialize threshold values to 0 and valley to zero
peak1_final = 0
peak2_final = 0
valley_final = 0

goodness = 0
goodness_indx = 0
# Distance between peaks >= 90
for i,g_i in enumerate(peaks_indx):
    # Since the indexes are arranged in ascending manner, iterate from the 
    # next value
    for j,g_j in enumerate(peaks_indx[(i+1):]):
        # Spacing between 2 thresholds is restricted to 90
       if g_j-g_i >= 90:
           mid_pnt = math.ceil((g_j+g_i) / 2)
           # we accept the valley around the midpoint of the 2 peaks
           for k,g_k in enumerate(valleys_indx) :
               if (g_k>g_i) and (g_k<g_j):
                   # Valley index shoul be 15 points to the left or right of mid value
                   if (g_k < mid_pnt+15) or (g_k > mid_pnt-15):
                       # If the valley is aound 15 points distance from 
                       # center, compute the "Peakiness"
                       
                       # Peakiness = min(Hst(g_i), Hist(g_j))/ Hist(g_k)
                       gdns = min(hist[g_i], hist[g_j]) / hist[g_k]
                   
                    # If the peakiness is greater than existing, 
                    # Pick the current thresholds and new peakiness
                   if (gdns > goodness):
                       print('enter',gdns)
                       goodness = gdns
                       goodness_indx = g_k
                       peak1_final = g_i
                       peak2_final = g_j
         
peak_img = np.copy(image)              
if goodness_indx != 0:
    for i in range(0,512,1):
        for j in range(0,512,1):
            if image[i][j] > hist[goodness_indx]:
                peak_img[i][j] = 255
            else:
                peak_img[i][j] = 0
                   
plt.imshow(peak_img, cmap='gray')
