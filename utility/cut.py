import pathlib
import os
from PIL import Image

parent_path = str(pathlib.Path(__file__).parent.resolve())

old_dir = os.path.join(parent_path, "tama_images")
new_dir = os.path.join(parent_path, "cc_tama_images")

if not os.path.exists(new_dir):
    os.makedirs(new_dir)

if not os.path.exists(old_dir):
    print("Make sure tama_images directory exists.")
    exit()

ls = os.listdir(old_dir)

for filename in ls:
    im = Image.open(os.path.join(old_dir, filename))
    crop = (10, 0, 310, 335)
    im_crop = im.crop(crop)
    new_imname = "cc_" + os.path.basename(filename)
    im_crop.save(os.path.join(new_dir, new_imname))
