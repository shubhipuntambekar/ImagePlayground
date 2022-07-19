# python3 jpeg_to_png folder_name/ new_folder/

# take all the images from folder_name
# convert all the images to png
# save them all in the new folder

import sys
import os

from PIL import Image

# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new_folder exist, if not create it.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the folder_name
# convert images to png
# save them to the new_folder
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{clean_name}.png", "png")
    print("all done!")


