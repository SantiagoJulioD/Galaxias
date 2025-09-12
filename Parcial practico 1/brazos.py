import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.ndimage import rotate,zoom

data = fits.open('NGC_3938_SDSS_g_bms2014.fits')

image_g = data[0].data

pa_mean = (0)*np.pi/180
eps_mean = 1-np.cos(0*np.pi/180)

corrected_image = rotate(image_g,pa_mean*180/np.pi,reshape=False)
corrected_image = zoom(corrected_image,(1/(1-eps_mean),1))

fig, ax = plt.subplots(figsize=(12,6))
im = ax.imshow(corrected_image,origin='lower',vmin=0,vmax=1,cmap='inferno')
fig.colorbar(im)
plt.show()