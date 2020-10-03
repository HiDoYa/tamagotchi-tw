import pathlib
import os
from PIL import Image, ImageOps, ImageFilter

parent_path = str(pathlib.Path(__file__).parent.resolve())

old_dir = os.path.join(parent_path, "tama_images")
imag_dir = os.path.join(parent_path, "imag_tama_images")
name_dir = os.path.join(parent_path, "name_tama_images")
desc_dir = os.path.join(parent_path, "desc_tama_images")

if not os.path.exists(imag_dir):
    print("Creating: {}".format(imag_dir))
    os.makedirs(imag_dir)

if not os.path.exists(name_dir):
    print("Creating: {}".format(name_dir))
    os.makedirs(name_dir)

if not os.path.exists(desc_dir):
    print("Creating: {}".format(desc_dir))
    os.makedirs(desc_dir)
    
if not os.path.exists(old_dir):
    print("Make sure tama_images directory exists.")
    exit()

def crop_save(im, filename, crop, name_cut=False, desc_cut=False):
    im_crop = im.crop(crop)
    if name_cut:
        im_crop = ImageOps.invert(im_crop)
        im_crop = im_crop.filter(ImageFilter.MaxFilter(3))
        im_crop = im_crop.convert('1')

        # Creates cleaner images but doesn't perform better for google ocr
        # fn = lambda x : 0 if x > 100 else 255
        # im_crop = im_crop.convert('L').point(fn, mode='1')

    if desc_cut:
        px = im_crop.load()
        for i in range(380):
            for j in range(5, 20):
                px[i,j] = (255, 255, 255)

            for j in range(45, 60):
                px[i,j] = (255, 255, 255)

            for j in range(86, 100):
                px[i,j] = (255, 255, 255)

            for j in range(128, 143):
                px[i,j] = (255, 255, 255)

    im_crop.save(filename)

ls = os.listdir(old_dir)

for filename in ls:
    print("Current file: {}".format(filename))
    im = Image.open(os.path.join(old_dir, filename))
    crop_save(im, os.path.join(imag_dir, filename), (10, 0, 310, 335))
    crop_save(im, os.path.join(name_dir, filename), (300, 30, 680, 120), name_cut=True)
    crop_save(im, os.path.join(desc_dir, filename), (300, 120, 680, 300), desc_cut=True)

