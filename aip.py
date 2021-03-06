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
    "edges of image are masked first (thickness = 116)"
    data[0:116,0:data.shape[1]] = 0
    data[116:data.shape[0], 0:116] = 0
    data[(data.shape[0]-116):data.shape[0], 116:data.shape[1]] = 0
    data[116:(data.shape[0]-116), (data.shape[1]-116):data.shape[1]] = 0
    "masked middle star"
    data[0:4612, 1425:1450] = 0
    data[218:261, 1388:1477] = 0
    data[115:142, 1386:1469] = 0
    data[142:162, 1409:1425] = 0
    data[142:147, 1449:1454] = 0
    data[116:152, 1450:1540] = 0
    data[123:133, 1289:1387] = 0
    data[311:320, 1021:1705] = 0
    data[315:372, 1411:1468] = 0
    data[319:346, 1314:1541] = 0
    data[426:438, 1104:1652] = 0
    data[434:472, 1366:1490] = 0
    circle(3204,1444,415)
    
def histogram(data_2):
    plt.xlim(3300,3550)
    plt.ylim(0,400000)
    plt.hist(data_2, bins=1000)
    plt.show()

bkgd = np.mean(data_2)

def max_pixel(data=data): 
    max_pix_index = np.unravel_index(data.argmax(), data.shape)
    if data.argmax() >= 3623.5:
        print("All is well")
    else:
        print("THIS DOES NOT COUNT")
    return max_pix_index


def magnitude(x,y,radius,localbkgd = bkgd, ZPinst=ZPinst):
    total_intensity = 0
    numberofpoints = 0
    cx, cy = x,y 
    x,y = np.ogrid[-radius: radius+1, -radius: radius+1]
    index = x**2 + y**2 <= radius**2
    if cx < data.shape[0]/2 and cx < radius:
        cx = radius
    if cy < data.shape[1]/2 and cy < radius:
        cy = radius
    if cx > data.shape[0]/2 and (data.shape[0] - cx) < radius:
        cx = data.shape[0] - radius - 1
    if cy > data.shape[1]/2 and (data.shape[1] - cy) < radius:
        cy = data.shape[1] - radius - 1
    area = data[cx-radius:cx+radius+1, cy-radius:cy+radius+1][index]
    for i in area:
        total_intensity += i
        if i != 0:
            numberofpoints += 1

    net_intensity = total_intensity - localbkgd*numberofpoints
    mag = -2.5*np.log10(net_intensity)
    m = ZPinst + mag
    return net_intensity, m

def circle(x,y,radius, data=data): 
    cx, cy = x,y
    y,x = np.ogrid[-radius: radius+1, -radius: radius+1]
    index = x**2 + y**2 <= radius**2
    if cx < data.shape[0]/2 and cx < radius:
        cx = radius
    if cy < data.shape[1]/2 and cy < radius:
        cy = radius
    if cx > data.shape[0]/2 and (data.shape[0] - cx) < radius:
        cx = data.shape[0] - radius - 1
    if cy > data.shape[1]/2 and (data.shape[1] - cy) < radius:
        cy = data.shape[1] - radius - 1
    data[cx-radius:cx+radius+1, cy-radius:cy+radius+1][index] = 0
        

def radius(x, y):
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

def realcentre(x,y, bkgd = bkgd):
    yplus = 0
    yminus = 0
    xplus = 0
    xminus =0
    while data[x, y + yplus] > bkgd:
        yplus +=1
    while data[x,y - yminus] > bkgd:
        yminus +=1
    while data[x + xplus, y] > bkgd:
        xplus +=1
    while data[x - xminus,y] > bkgd:
        xminus += 1
    
    xchange = (xplus - xminus)/2
    ychange = (yplus - yminus)/2

    newx = int(x+xchange)
    newy = int(y+ychange)
    
    return newx,newy, (xplus+xminus)/2, (yplus+yminus)/2

def edgethickness(x, y,axis, value = 3421):
    i=0
    if axis == 1:
        while data[y, x-i] == value:
            i += 1
    if axis == 2:
        while data[y+i, x] == value:
            i += 1   
    return i




#plt.figure()
#plt.imshow(image_data, cmap='gray')
#plt.colorbar()






