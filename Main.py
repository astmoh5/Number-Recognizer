from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from random import randint, random

img = tuple
nums = [
    (np.asarray(Image.open('nums/zero_0.jpg')), np.asarray(Image.open('nums/zero_1.jpg'))),
    (np.asarray(Image.open('nums/one_0.jpg')), np.asarray(Image.open('nums/one_1.jpg')))
    ]

img[1] = randint(0,1)
img[0] = nums[img[1]][randint(0,len(nums[img[1]]))]
l1_0, l1_1, l1_2, l1_3, l1_4, l1_5, l1_6, l1_7, l1_8, l1_9, l1_10 = random, random, random, random, random, random, random, random, random, random
out = int
accuracy = 50
results = list
[
    #input
    img[0],

    #Layer1
    [
        l1_0, l1_1, l1_2, l1_3, l1_4, l1_5, l1_6, l1_7, l1_8, l1_9, l1_10
    ],

    #output     
    out

]

while accuracy<90:



    if out == img[1]:
        results.append(1)
    else: results.append(0)
    accuracy = sum(results)/len(results)
