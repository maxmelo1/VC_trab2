import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import os


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

    if p>0:
        imagePadded = np.zeros((width + p*2, height + p*2))
        imagePadded[int(p):int(-1 * p), int(p):int(-1 * p)] = img
    else:
        imagePadded = img

    for y in range(height):
        if y > height-kheight:
            break
        if y % s == 0:
            for x in range(width):
                if x > width - kwidth:
                    break
                try:
                    if x % s == 0:
                        output[x, y] = (kernel*imagePadded[x:x+kwidth, y: y+kheight]).sum()
                except:
                    break
    return output

img    = Image.open('imgs/noisy.jpg')
img    = np.array(img)
#kernel = np.array([[-1,-2,-1], [0,0,0], [1,2,1]], dtype='uint8')
kernel = np.ones((3,3), dtype='uint8')/9

res = convolution(img, kernel)


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
res = convolution(img, kernel)

plt.imshow(res, cmap='gray')
plt.show()
res = Image.fromarray(res)
res.save('out/a_5_5.png')