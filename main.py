import os
import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rotate
from deskew import determine_skew

_files = os.listdir("skewds")  # get a list of all filenames

for i in _files:  # loop through all files
    image = io.imread("skewds/" + i)
    grayscale = rgb2gray(image)
    angle = determine_skew(grayscale)
    rotated = rotate(image, angle, resize=True) * 255
    io.imsave("deskewds/" + i, rotated.astype(np.uint8))
