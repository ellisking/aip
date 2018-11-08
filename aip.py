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

def histogram(data_2):
    plt.xlim(3300,3550)
    plt.ylim(0,400000)
    plt.hist(data_2, bins=1000)
    plt.show()

bkgd = np.mean(data_2)
print(max(data_list))
print(data_list.count(max(data_list))) #number of occurences of max pixel

def max_pixel(data): 
    max_pix_index = np.unravel_index(data.argmax(), data.shape)
    return max_pix_index

def magnitude(x,y,radius,localbkgd = bkgd, ZPinst=ZPinst):
    total_intensity = 0
    numberofpoints = 0
    cx, cy = x,y 
    y,x = np.ogrid[-radius: radius+1, -radius: radius+1]
    index = x**2 + y**2 <= radius**2
    for i in data[cy-radius:cy+radius+1, cx-radius:cx+radius+1][index]:
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
    c = data[cy-radius:cy+radius+1, cx-radius:cx+radius+1][index]
    return c

def local_background(x, y):
   "get radius, local background level, max value"
   max_value = data[y,x]
   radius = 0         
   meanpoints = []   
   means = data[y, x]
   meanpoints.append(means)
   
   radius = 1
   means = np.mean((data[y, x +  radius],data[(y + radius),x],data[y,x - (radius)],data[y - (radius ),x]))
   meanpoints.append(means)
   
   while (abs(meanpoints[-1] - meanpoints[-2])) > 5 and meanpoints[-1] > 3400:
       radius +=1                
       means = np.mean((data[y, x +  radius],data[(y + radius),x], data[y,x - (radius)],data[y - (radius ),x]))
       meanpoints.append(means)
             
   return radius, meanpoints[-1], max_value



