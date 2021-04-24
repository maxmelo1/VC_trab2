import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def convolution(img, kernel):
    '''
    It runs a convolution in the img based on a given kernel
    img a PIL image instance
    kernel an array with odd dimensions
    returns an convoluted image or None if no convolution can be applied
    '''

    p = 1
    s = 1

    kwidth = kernel.shape[0]
    kheight = kernel.shape[1]
    ks = kwidth // 2
    
    width  = img.shape[0]
    height = img.shape[1]

    width_out  = int(((width-kwidth + 2*p) / s) + 1)
    height_out = int(((height-kheight + 2*p) / s) + 1)
    


    assert kwidth%2==1, "wrong shape, exiting"
    assert kheight%2==1, "wrong shape, exiting"
    assert kwidth==kheight, "wrong shape, exiting"

    output = np.zeros((width_out, height_out), dtype='uint8')

img    = Image.open('imgs/noisy.jpg')
img    = np.array(img)
kernel = np.array([[0,1,0], [1,1,1], [0,1,0]], dtype='uint8')


convolution(img, kernel)
    