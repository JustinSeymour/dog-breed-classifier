#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Justin Seymour
# DATE CREATED: 19 January 2020                                 
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
from os import path

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
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    pet_images_name_list = listdir(image_dir)
    
    
    results_dic = dict()
    
    results_dic_length = len(results_dic)
    
    
    filenames= pet_images_name_list
    # pet_labels = ["beagle", "boston terrier"]
    
    # Adds a new key-value to the results_dic, only if it is not present
    # Creates a list that contains the pet_image label
    for name in range(0, len(filenames), 1):
        if filenames[name] not in results_dic or f:
            
            # If file is a hidden file, skip this iteration
            if filenames[name].startswith("."):
                continue
            
            # Transform label to lowercase 
            lower_pet_image = filenames[name].lower()
            
            
            # Trim file extension from the file name
            trimmed_pet_image = path.splitext(lower_pet_image)
            
        
            # Split label at the underscore
            word_list_pet_image = trimmed_pet_image[0].split("_")
        
            pet_name = ""
        
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_name += word + " "

            pet_name = pet_name.strip()
        
            
            results_dic[filenames[name]] = [pet_name]
            
        else:
            print("Warning: Key=", file_names[name]), "is already present in the results_dic with value=", results_dic[file_names[name]]
    
    # Loop through dic and print all keys and associated values to console
#     print("\nPrinting key-value pairs in the dictionary results_dic:")
#     for key in results_dic:
#         print("Filename=", key," Pet Label=", results_dic[key][0])
        
   
     
    return results_dic
