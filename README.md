# Computer-Vision-8820
Assignment 3 : Thresholding
Peakiness detection
Strategy : Threshold for max peaks is set as 2000. And threshold for valleys is set to 400 g_i initialized to 0 and
g_j initialized to 0 and
g_k initialized to 0 ; where g_i, g_j are the peaks and g_k is the valley in between.
Goodness and goodness_indx are initialized to 0. Since, peak index values are already arranged in ascending order, we iterate through it twice, outer loop for g_i and inner loop for g_j and valley is restricted to be 15 steps away from midpoint between the peaks to left or right. Goodness is then measured by dividing the minimum value between g_i and g_j by valley value.
This is compared with the previous goodness value and if it’s better, goodness index, threshold values, valley value are reassigned to current values.

 Iterative Thresholding
Strategy : Threshold is initialized to the mean value of intensity. All the pixels are divided into 2
regions based on if they are greater or smaller than the initial value. Then we compute means of 2 regions and mean of the 2 means. Again the image is segmented into regions so on as long as threshold computed is not equal to the previous value. Final threshold is used to convert the image to binary by comparing each pixel intensity to the threshold computed.

Adaptive Thresholding :
Strategy : divide the image into four equal parts. Apply iterative threshold on each part and merge them finally.

Double Thresholding :
Strategy ; Initial thresholds are mean and mean of values between 127 and 256 on histogram. Divide image into 3 regions. R2 is between threhsold1 and threshold2. Assign pixels in region2 with neighbors all belonging to R1 to R1. Assign remaining R2 pixels to R3. Finally, pixels in R1 are assigned 255 and the rest are assigned 0.
