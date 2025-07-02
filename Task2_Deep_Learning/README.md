# Task 2: Deep Learning with TensorFlow – MNIST Digit Classification 

##  Overview

This task involves building and training a Convolutional Neural Network (CNN) using TensorFlow to classify handwritten digits from the MNIST dataset. The goal was to achieve over **95% accuracy** on the test set and visualize predictions.

---

##  Objectives

- Load and preprocess the MNIST dataset.
- Design and implement a CNN architecture using TensorFlow/Keras.
- Train the model and evaluate its performance.
- Visualize predictions on 5 sample images.

---

## Results

- **Test Accuracy Achieved**: >95%
- Evaluation metrics and training accuracy were printed in the terminal.


## Model Architecture

- **Input Layer**: 28x28 grayscale images
- **Conv2D**: 32 filters (3x3), ReLU
- **MaxPooling2D**: (2x2)
- **Conv2D**: 64 filters (3x3), ReLU
- **MaxPooling2D**: (2x2)
- **Flatten**
- **Dense**: 64 units, ReLU
- **Dropout**: 0.5
- **Output Layer**: 10 units (Softmax)

---

##   File Structure

