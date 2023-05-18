# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-A3kep4MqffI9Q5rfbpme7sa0xf1V04S
"""

import streamlit as st
import tensorflow as tf
import requests
import io


@st.cache(allow_output_mutation=True)
def load_model():
    model_url = "https://github.com/ybluerizza/Streamlit/raw/main/Streamlit/final_model.h5"
    response = requests.get(model_url)
    model_data = response.content

    # Save the model data to a temporary file
    model_path = "/tmp/final_model.h5"
    with open(model_path, "wb") as f:
        f.write(model_data)

    # Load the model from the saved file
    model = tf.keras.models.load_model(model_path)

    return model

model = load_model()
st.write("""
# Image Classification System"""
)
file=st.file_uploader("Choose image photo from computer",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(32,32)
    image=ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)