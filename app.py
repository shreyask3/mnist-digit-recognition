#!/usr/bin/env python
# coding: utf-8
from flask import Flask, render_template, request
import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.models import load_model
from PIL import Image
app = Flask(__name__, template_folder='templates')
@app.route('/')
def upload_file():
   return render_template('index.html')

@app.route('/uploader', methods=['POST'])
def upload_image_file():
    model=load_model('model/model.h5')
    if request.method == 'POST':
        img = Image.open(request.files['file'].stream).convert("L")
        img = img.resize((28, 28))
        im2arr = np.array(img)
        im2arr = im2arr / 255
        im2arr = im2arr.reshape(1, 28, 28, 1)
        prob = model.predict(im2arr)
        pred = np.argmax(prob)
        return 'Predicted Number: '+ str(pred)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4040)

