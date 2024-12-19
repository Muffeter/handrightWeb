# coding: utf-8
from PIL import Image, ImageFont
from multiprocessing import Pool
from handright import Template, handwrite
import datetime


def run(text: str, template: Template):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp}"

    images = handwrite(text, template)
    for i, im in enumerate(images):
        assert isinstance(im, Image.Image)
        im.save(f"static/{filename}.png")
    return filename
