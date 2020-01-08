import cv2
import numpy as np
import os

folder_name = input("Please enter Folder name: ")
output_folder_name = "output"
os.mkdir("output")

all_images_temp = os.listdir(folder_name)    # Read all files in folder
all_images = []                              # Filter only Images
for img in all_images_temp:
    if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg") or img.endswith(".tiff"):
        all_images += [img]

for img in all_images:
    x = cv2.imread(folder_name + "/" + img)
    #cv2.imshow(x)

    #Orginal Values in [Blue, Green, Red]: [208, 242, 201]
    lower = np.array([200,240,190]) 
    upper = np.array([210,250,210]) 
    # Here we are defining range of color in BGR

    # This creates a mask of desired coloured objects found in the frame. 
    mask = cv2.inRange(x, lower, upper) 
    #cv2.imshow(mask)

    output_img = cv2.bitwise_and(x,x,mask = mask)
    cv2.imwrite(output_folder_name +"/"+ img, output_img)

