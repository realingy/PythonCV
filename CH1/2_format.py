#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:ingy time:2019/9/18

from PIL import Image
import os


infile = Image.open("image/car.jpg")
outfile = os.path.splitext(infile)[0] + ".png"
if infile != outfile:
    try:
        Image.open(infile).save(outfile)
    except IOError:
        print("cannot convert", infile)


