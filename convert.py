from PIL import Image
import threading
import glob
import os
#a script to resize images
#to resize images just put in the folder containing images you want to resize
path = os.getcwd()
save_dir = os.path.join(path, 'resized')
if(!os.path.exists(save_dir)):
    os.makedirs(save_dir)
dirs = os.listdir(path)
for i, dir in enumerate(dirs):
    file = os.path.join(path, dir)
    f, e = os.path.splitext(file)
    if(os.path.isfile(file) and e == '.jpg'):
        img = Image.open(file)
        imResize = img.resize((300,225), Image.ANTIALIAS)
        imResize.save(os.path.join(save_dir, f.split('\\')[-1]+'_r.jpg'), 'JPEG', quality=90)
        print(i+'/'+len(dirs), flush=True)
