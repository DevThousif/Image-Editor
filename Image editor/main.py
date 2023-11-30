from PIL import Image, ImageEnhance, ImageFilter
import os
os.chdir('C:\Coding\python\Image editor') # input your file directory

path = "./images" # previous image
pathOut = "/editedimages" # edited image

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # sharpening
    edit = img.filter(ImageFilter.SHARPEN)

    # contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

   

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')