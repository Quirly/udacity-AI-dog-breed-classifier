#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Susanne Wuerl
# DATE CREATED: 01.05.2020                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    #create new empty dictionary and a list with all image file names named dirs
    #dirs will be the key of the new dictionary results_dic
    #petlabel will be the file name after processing, the so called label
    #the label will be the value of the new dictionary results_dic
    #the output of this function is the new dictionary (return)
    results_dic=dict()
    dirs=list(listdir(image_dir))
    doglabels=dirs
    petlabels=[]
    #print(dirs)
    for doglabel in doglabels:
        petlabel=""
        for onelabel in doglabel:
            if not onelabel.isdigit():
               petlabel=(petlabel+onelabel)    
        petlabels.append(petlabel.replace("_"," ").replace(" .jpg","").lower().split(", "))
    results_dic=dict(zip(dirs,petlabels))
   
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic#petlabels #zip(dirs,dogeglabels)

if __name__=='__main__':
    folder='pet_images'
    ergebnis=get_pet_labels(folder)
    print(ergebnis)
    