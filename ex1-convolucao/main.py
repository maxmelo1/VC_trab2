import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import os
import math

def getGaussianKernel(sigma=0.5):
    size= int(6*sigma)
    size = size if size%2==1 else size + 1

    s = size//2
    soma =0
    idx=0

    kernel = np.zeros((size,size))
    print(size)
    

    for x in range(-s, 1+s):
        idy = 0
        for y in range(-s, 1+s):
            kernel[idx, idy] = (1./(2*math.pi*sigma**2))*math.exp( - (x**2+y**2)/(2*sigma**2))
            soma += kernel[idx, idy]
            idy += 1
        idx +=1

    print(kernel)
    print('soma', soma)
    
    kernel_n = kernel / soma
    print(kernel_n)

    # plt.imshow(kernel)
    # plt.show()

    # plt.imshow(kernel_n)
    # plt.show()

    return kernel

def convolution(img, kernel, s=1, p=1):
    '''
    It runs a convolution in the img based on a given kernel
    img: a np array representing an image instance
    kernel: an array with odd dimensions
    s: convolution stride
    p: convolution padding. Zero fill is applied.
    returns an convoluted image or None if no convolution can be applied
    '''
    
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

    if p>0:
        imagePadded = np.zeros((width + p*2, height + p*2))
        imagePadded[int(p):int(-1 * p), int(p):int(-1 * p)] = img
    else:
        imagePadded = img

    for y in range(0, height_out, s):
        for x in range(0, width_out, s):
            output[x, y] = (kernel*imagePadded[x:x+kwidth, y: y+kheight]).sum()
                
    return output

img    = Image.open('imgs/noisy.jpg')
img    = np.array(img)
#kernel = np.array([[-1,-2,-1], [0,0,0], [1,2,1]], dtype='uint8')
kernel = np.ones((3,3), dtype='uint8')/9

res = convolution(img, kernel, p=1)


#cvres = cv2.filter2D(img, -1, kernel)
#plt.imshow(cvres, cmap='gray')
#plt.show()

if not os.path.exists('out'):
    os.mkdir('out')


plt.imshow(res, cmap='gray')
plt.show()
res = Image.fromarray(res)
res.save('out/a_3_3.png')


kernel = np.ones((5,5), dtype='uint8')/25
res = convolution(img, kernel=kernel, p=2)


plt.imshow(res, cmap='gray')
plt.show()
res = Image.fromarray(res)
res.save('out/a_5_5.png')

kernel = getGaussianKernel(1)
res = convolution(img, kernel=kernel, p=3)
plt.imshow(res, cmap='gray')
plt.show()
res = Image.fromarray(res)
res.save('out/b_sigma_1.png')

kernel = getGaussianKernel(2)
res = convolution(img, kernel=kernel, p=6)
plt.imshow(res, cmap='gray')
plt.show()
res = Image.fromarray(res)
res.save('out/b_sigma_2.png')

kernel = getGaussianKernel(3)
res = convolution(img, kernel=kernel, p=9)
plt.imshow(res, cmap='gray')
plt.show()
res = Image.fromarray(res)
res.save('out/b_sigma_3.png')

# print(img.shape)
# print(res.shape)