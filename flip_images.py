
"""
expanding the dataset by horizontal mirroring
"""

from PIL import Image, ImageEnhance
import numpy as np
import os


#Mirror horizontally and up and down using the PIL function
def ImgLRMirror(Img):
    return Img.transpose(Image.FLIP_LEFT_RIGHT)

def ImgTBMirror(Img):
    return Img.transpose(Image.FLIP_TOP_BOTTOM)

src_path="E:/Files/Dataset/"

mirror_save_path="E:/Files/flip_Dataset/"

img_list=os.listdir(src_path)
print(len(img_list))

for j in range(0,len(img_list)):
    img_path=os.path.join(src_path,img_list[j])
    if os.path.isfile(img_path):
        Img=Image.open(img_path)
        mirror_imglrm=ImgLRMirror(Img)
        save_mirror_pathlrm = os.path.join(mirror_save_path, 'flip_' + img_list[j])
        mirror_imglrm.save(save_mirror_pathlrm)



