import sys
import os
from PIL import Image, ImageFilter

old_dir = sys.argv[1]  # input old directory
new_dir = sys.argv[2]  # input new directory


dir_list = os.listdir(old_dir)  # list all images in old directory

# check if new directory already exists

if os.path.exists(new_dir):
    pass
else:
    os.mkdir(new_dir)
new_dir_list = os.listdir(new_dir)
# converting images in old directory to png

for img in dir_list:
    filename, extension = os.path.splitext(img)
    f_new = filename + '.png'
    try:
        if f_new not in new_dir_list:
            new_file = new_dir + f_new
            old_img_filepath = old_dir + filename + extension
            img_new = Image.open(old_img_filepath)
            img_new.save(new_file, 'png')
            print(f'{filename} image has been converted to {f_new}')
        else:
            print(f'{filename} has already been converted!')
    except:
        print('Cannot process images')
