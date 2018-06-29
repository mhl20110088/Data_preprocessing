#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#import skimage.io as io
import scipy.io as io
import h5py
import os
from PIL import Image
f=h5py.File("D:\\documents\\Downloads\\nyu_depth_v2_labeled.mat")
labels=f["depths"]
labels=np.array(labels)

path_converted='D:\\documents\\Downloads\\nyu_depth'
if not os.path.isdir(path_converted):
    os.makedirs(path_converted)
for i in range(len(labels)):
    depth=labels[i]
    depth_ = np.empty([480, 640, 3])
    depth_[:, :, 0] = depth[:, :].T
    depth_[:, :, 1] = depth[:, :].T
    depth_[:, :, 2] = depth[:, :].T
    depth_=depth_/4.0
    #depth_1 = Image.fromarray(np.uint8(depth_))
    iconpath='D:\\documents\\Downloads\\nyu_depth\\'+str(i)+'.mat'
    io.savemat (iconpath, {'depth_':depth_})

"""
import skimage.io as io
import numpy as np
import h5py

# data path
path_to_depth = 'D:\\documents\\Downloads\\nyu_depth_v2_labeled.mat'

# read mat file
f = h5py.File(path_to_depth)

# read 0-th image. original format is [3 x 640 x 480], uint8
img = f['images'][0]

# reshape
img_ = np.empty([480, 640, 3])
img_[:,:,0] = img[0,:,:].T
img_[:,:,1] = img[1,:,:].T
img_[:,:,2] = img[2,:,:].T

# imshow
img__ = img_.astype('float32')
io.imshow(img__/255.0)
io.show()


# read corresponding depth (aligned to the image, in-painted) of size [640 x 480], float64
depth = f['depths'][0]

# reshape for imshow
depth_ = np.empty([480, 640, 3])
depth_[:,:,0] = depth[:,:].T
depth_[:,:,1] = depth[:,:].T
depth_[:,:,2] = depth[:,:].T

io.imshow(depth_/4.0)
io.show()
"""