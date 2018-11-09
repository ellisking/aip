# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from astropy.io import fits
from statistics import mode
import matplotlib.pyplot as plt
import numpy as np

hdulist=fits.open('C:\\Users\\tinyb\\Documents\\lab\\aip\\A1_mosaic\\A1_mosaic.fits')
ZPinst = hdulist[0].header["MAGZPT"]
data=hdulist[0].data
data_list=list(np.ndarray.flatten(data))
data_2=[]
[data_2.append(i) for i in data_list if i < 3550]
unique = []
[unique.append(item) for item in data_2 if item not in unique]

def mask(data=data):
    data[657,2530]=0
    circle(3443,2562,2)
    
def histogram(data_2):
    plt.xlim(3300,3550)
    plt.ylim(0,400000)
    plt.hist(data_2, bins=1000)
    plt.show()

bkgd = np.mean(data_2)

def max_pixel(data): 
    max_pix_index = np.unravel_index(data.argmax(), data.shape)
    return max_pix_index

def magnitude(x,y,radius,localbkgd = bkgd, ZPinst=ZPinst):
    total_intensity = 0
    numberofpoints = 0
    cx, cy = x,y 
    x,y = np.ogrid[-radius: radius+1, -radius: radius+1]
    index = x**2 + y**2 <= radius**2
    for i in data[cx-radius:cx+radius+1, cy-radius:cy+radius+1][index]:
        total_intensity += i
        numberofpoints += 1

    net_intensity = total_intensity - localbkgd*numberofpoints
    mag = -2.5*np.log10(net_intensity)
    m = ZPinst + mag
    return net_intensity, m

def circle(x,y,radius, data=data): 
    cx, cy = x,y
    y,x = np.ogrid[-radius: radius+1, -radius: radius+1]
    index = x**2 + y**2 <= radius**2
    data[cx-radius:cx+radius+1, cy-radius:cy+radius+1][index] = 0
    

def local_background(x, y):
   max_value = data[x,y]
   radius = 0         
   meanpoints = []   
   means = max_value
   meanpoints.append(means)
   
   radius = 1
   means = np.mean((data[x, y +  radius],data[(x + radius),y],data[x,y - (radius)],data[x - (radius ),y]))
   meanpoints.append(means)
   
   while (abs(meanpoints[-1] - meanpoints[-2])) > 5 and meanpoints[-1] > 3400:
       radius +=1                
       means = np.mean((data[x, y +  radius],data[(x + radius),y],data[x,y - (radius)],data[x - (radius ),y]))
       meanpoints.append(means)
             
   return radius, meanpoints[-1], meanpoints[0]





#plt.figure()
#plt.imshow(image_data, cmap='gray')
#plt.colorbar()





