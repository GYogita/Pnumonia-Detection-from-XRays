#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image
from tensorflow.keras.models import load_model


# In[2]:


model=load_model('pnumonia pred model.keras')


# In[4]:


class_names=['Normal', 'Pneumonia']
st.title('Pneumonia Detection from Chest X-ray')
st.write('Upload chest x-ray image')

uploaded_file=st.file_uploader('Choose X-ray image', type=['jpg','png','jpeg'])

if uploaded_file is not None:
    img= Image.open(uploaded_file).convert('RGB')
    st.image(img,caption='Image uploaded successfully')

    # Preprocessing
    img=img.resize((32,32)) #resize
    img_array=image.img_to_array(img)/255.0 # rescale
    img_array=np.expand_dims(img_array, axis=0) #adding 1 dimension as it is a single data image

    prediction=model.predict(img_array)
    confidence=float(prediction[0][0])

    if confidence>=0.5:
        st.error('Prediction: Pneumonia Detected')
    else:
        st.success('Prediction: No Pneumonia Detected')


# In[ ]:




