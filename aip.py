# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
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
#print(hdulist.info())
#print(hdulist[0].data[1,1])
data=hdulist[0].data
data=np.ndarray.flatten(data)
data=list(data)
data_2=[]
[data_2.append(i) for i in data if i < 3550]
#plt.xlim(3300,3550)
#plt.ylim(0,400000)
unique = []
[unique.append(item) for item in data_2 if item not in unique]
#plt.hist(data_2, bins=1000)
print(np.mean(data_2))
print(max(data))
print(data.count(max(data)))
#maskdata = [x for x in data_2 if x != mode(data)]


