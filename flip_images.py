
"""
用水平镜像的方式扩充数据集后，得到1004*2=2008张图像
"""

from PIL import Image, ImageEnhance
import numpy as np
#import imutils
import os




#用PIL的函数进行水平以及上下镜像
def ImgLRMirror(Img):
    return Img.transpose(Image.FLIP_LEFT_RIGHT)

def ImgTBMirror(Img):
    return Img.transpose(Image.FLIP_TOP_BOTTOM)

src_path="E:/March_Files/Cervical_vertebra_Task/20240802_rerun_5_algorithms/Cervical_vertebra1_2_3_4_5_6_Dataset/"

mirror_save_path="E:/March_Files/Cervical_vertebra_Task/20240802_rerun_5_algorithms/flip_Cervical_vertebra1_2_3_4_5_6_Dataset/"

img_list=os.listdir(src_path)
print(len(img_list))

for j in range(0,len(img_list)):
    #print(i)
    img_path=os.path.join(src_path,img_list[j])
    if os.path.isfile(img_path):
        Img=Image.open(img_path)
        #lrm是水平翻转
        mirror_imglrm=ImgLRMirror(Img)
        #mirror_imgtbm=ImgTBMirror(Img)
        #save_mirror_pathlrm=os.path.join(mirror_save_path,'mirror_lrm_'+img_list[j])
        save_mirror_pathlrm = os.path.join(mirror_save_path, 'flip_' + img_list[j])
        #save_mirror_path_tbm=os.path.join(mirror_save_path,'mirror_tbm_'+img_list[j])
        mirror_imglrm.save(save_mirror_pathlrm)
        #mirror_imgtbm.save(save_mirror_path_tbm)



