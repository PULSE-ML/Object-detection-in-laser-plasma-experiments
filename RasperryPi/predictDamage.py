import torch
import os
import glob
# from IPython.display import Image, clear_output  # to display images

testImagePath = 'home/pi/yolov5/detectDamage'
os.path.dirname(os.path.realpath(__file__))
print(testImagePath)


imageList =  glob.glob("{}/*.png".format(testImagePath))
!python detect.py --weights home/pi/yolov5/detectDamage/damageDetection.pt --img 416 --conf 0.1 --source imageList --save-txt --hide-conf --hide-labels

#display inference on ALL test images

# import glob
# from IPython.display import Image, display

# for imageName in glob.glob('/content/yolov5/runs/detect/exp/*.jpg'): #assuming JPG
#     display(Image(filename=imageName))
#     print("\n")