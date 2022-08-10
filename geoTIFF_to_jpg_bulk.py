'''
Python geoTIFF (.tif) to .jpg converter
Created to convert USGS .tif topography files to .jpg images
Requires: numpy, PIL, rasterio
USGS Downloader: https://apps.nationalmap.gov/downloader/
    - Select map area for height data
    - Chose "Elevation Product (3DEP)" in desired resolution
    - Click "Find Products"
    - Download .tif files and save to drive
'''

# Required Libraries
import os

import numpy as np
from PIL import Image
import rasterio
from rasterio.plot import show
def convert(drive, fn):
    # Join drive and fn
    fp = os.path.join(drive, fn)

    # Convert data to np array
    with rasterio.open(fp, 'r') as ds:
        arr = ds.read()

    # Define .jpg save location
    sn = fn[:-3]+'jpg'
    sp = os.path.join(drive, sn)

    # Range needs to be between 0 and 255 to be converted to image file
    arr = np.interp(arr, (arr.min(), arr.max()), (0, 255))

    # Reshape 3d array to 2d array
    arr = arr.reshape(len(arr[0][0]), len(arr[0][1]))

    # Convert np array to image w/ PIL and save to original location
    img = Image.fromarray(arr)

    # convert to RGB mode for saving
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Save .jpg image
    img.save(sp)


if __name__ == '__main__':
    # Set .tif file location
    drive = r'C:\Users\Jon\Desktop\usgs_utah'
    for fn in os.listdir(drive):
        if fn.endswith(".tif"):
            convert(drive, fn)
