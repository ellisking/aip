# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

hdulist=fits.open('C:\\Users\\tinyb\\Documents\\lab\\aip\\A1_mosaic\\A1_mosaic.fits')
print(hdulist.info())
print(hdulist[0].data[1,1])
data=hdulist[0].data
data=np.ndarray.flatten(data)
#plt.xlim(3300,3600)
plt.hist(data, bins='auto')
#mahesh = np.histogram(a=hdulist[0].data, bins=10000)
#plt.


#plt.figure()
#plt.imshow(image_data, cmap='gray')
#plt.colorbar()

