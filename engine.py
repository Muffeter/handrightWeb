# coding: utf-8
from PIL import Image, ImageFont
from multiprocessing import Pool
from handright import Template, handwrite


def run(text:str, template:Template):
    images = handwrite(text, template)
    for i, im in enumerate(images):
        assert isinstance(im, Image.Image)
        im.save(f"static/out{i}.png")