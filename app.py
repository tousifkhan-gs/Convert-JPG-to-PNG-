from PIL import Image
import os
import sys


image_folder = sys.argv[1]
out_folder = sys.argv[2]


if not os.path.exists(out_folder):
    os.mkdir(out_folder)
    
    
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{out_folder}{clean_name}.png', 'png')
    print('all done!')
