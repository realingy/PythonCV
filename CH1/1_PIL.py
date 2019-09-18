#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:ingy time:2019/9/18

# http://effbot.org/imagingbook/

from PIL import Image

# Open, rotate, and display an image (using the default viewer)
im = Image.open('image/car.jpg') # 读取一幅图像
im2 = Image.open('image/car.jpg').convert('L') # 转换成灰度图
# im.rotate(45).show() # 旋转并显示
# im2.show() # 显示


# Create thumbnails
import glob, os

size = 128, 128

for infile in glob.glob("image/*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    # im.thumbnail(size, Image.ANTIALIAS)
    # im.save(file + ".thumbnail", "JPEG")


# Image.new(mode, size, color) ⇒ image
im = Image.new("RGB", (512, 512), "red")
# im.show()


# Image.blend(image1, image2, alpha) ⇒ image
im1 = Image.open('image/mogu.jpg')
im2 = Image.open('image/rain.jpg')
alpha = 0.5
# out = image1 * (1.0 - alpha) + image2 * alpha
out = Image.blend(im1, im2, alpha) # 融合
out.show()

