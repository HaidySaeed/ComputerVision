#!/usr/bin/env python
# coding: utf-8

# In[30]:


import glob
import cv2
import matplotlib.pyplot as plt
from skimage.io import imread,imshow,imsave
import os
import numpy as np
import random
from sklearn.model_selection import train_test_split
import statistics as s
from sklearn.datasets import make_blobs
import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.utils import to_categorical
from keras.utils import np_utils


# In[31]:


#img=cv2.imread("Depuy.1.jpg")


# In[32]:


file = "Cofield\\*.jpg"
file2 = "Depuy\\*.jpg"
file3 = "Tornier\\*.jpg"
file4 = "Zimmer\\*.jpg"


# In[33]:


image = cv2.imread(file)
image2 = cv2.imread(file2)
image3 = cv2.imread(file3)
image4 = cv2.imread(file4)


# In[34]:


images = [cv2.imread(image) for image in glob.glob(file)]
images2 = [cv2.imread(image) for image in glob.glob(file2)]
images3 = [cv2.imread(image) for image in glob.glob(file3)]
images4 = [cv2.imread(image) for image in glob.glob(file4)]
images[0].shape


# In[35]:


x = []
y = []


# In[36]:


for i in range(0,len(images)):
    images[i] = cv2.resize(images[i], (250, 250))
    norm = (images[i] - np.mean(images[i])) / np.std(images[i])
    x.append(norm)
    y.append(0)
for i in range(0,len(images2)):
    images2[i] = cv2.resize(images2[i], (250, 250))
    norm = (images2[i] - np.mean(images2[i])) / np.std(images2[i])
    x.append(norm)
    y.append(1)
for i in range(0,len(images3)):
    images3[i] = cv2.resize(images3[i], (250, 250))
    norm = (images3[i] - np.mean(images3[i])) / np.std(images3[i])
    x.append(norm)
    y.append(2)
for i in range(0,len(images4)):
    images4[i] = cv2.resize(images4[i], (250, 250))
    norm = (images4[i] - np.mean(images4[i])) / np.std(images4[i])
    x.append(norm)
    y.append(3)


# In[37]:


print(len(y))
print (len(x))


# In[38]:


X = np.array(x).reshape(-1, 250, 250, 3)
X = X.astype('float32')
Y = np_utils.to_categorical(y, 4)
print (X.shape, Y.shape)


# In[39]:


x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,shuffle=True)


# In[43]:


model = tf.keras.Sequential([
tf.keras.layers.Conv2D(32, (3,3), padding='same', activation=tf.nn.relu,
input_shape=(250, 250, 3)),
tf.keras.layers.MaxPooling2D((2, 2), strides=2),
tf.keras.layers.Conv2D(32, (3,3), padding='same', activation=tf.nn.relu),
tf.keras.layers.MaxPooling2D((2, 2), strides=2),
tf.keras.layers.Dropout(0.5),
tf.keras.layers.Flatten(),
tf.keras.layers.Dense(128, activation=tf.nn.relu),
tf.keras.layers.Dense(4, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=15)


# In[45]:


model.evaluate(x_test, y_test)


# In[ ]:




