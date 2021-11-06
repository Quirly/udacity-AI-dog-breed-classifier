# udacity-dog-breed-classifier
Python application to identify dog breeds by uploading images using three pretrained neural networks (Nanodegree Project 1: Udacity AI Programming with Python)

## purpose
Building a Python application for image classification within Udacity nanodegree program 'AI Programmming with Python' 

## disclaimer
A ready-to-use classifier is used

## contents
* classifies pet images 
* uses a pretrained CNN model
* compares classification to true identity oft the pets (true identity is part of filename)
* outputs statistics how well the respective CNN performed
* user can choose between three CNN architectures to evaluate classification performance

## preparation
* install Python 3 or newer
* ensure that PIL is installed
* clone directory containing all files
* ensure that folder 'uploaded images' is present

## how to classify images

### input: prepare your image
* choose an image of a pet you find in the internet
* **ensure that the image file is a jpeg-format or has been converted to jpeg-format**
* **renaming the file is not sufficient, you need to convert it if it is not jpeg-format**
* put the jpeg-file in folder 'uploaded images'
* **rename the image follow this naming convention: petname_imagenumber.jpg** (image number can be chosen by you)

### run script/do classify
* run check_images.py in Python shell by typing in command _python check_images.py_

### output: evaluate performance and statistics
* classification performance (time needed for classification, each architecture can be different)
* classification statistics (Number of images classified, number of dog images, number of not-dog-images, number of matches, number of correct dog matches, number of correct dog breed matches, percentage of matched images, percentages of correctly as dogs classified images, number of correctly classified dog breed images, number of not-dog-images correctly classified, percentage of not-dogs correctly classified)
* for further analysis/follow up: showing names of all misclassified images that were classified as dogs but are not dogs
* for furter analysis/follow up: showing misclassified images with dog breeds that were not recognized by the model as dogs

  
