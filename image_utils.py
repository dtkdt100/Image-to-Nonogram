import PIL
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from PIL.ImageFont import ImageFont
from tabulate import tabulate
import tkinter as tk
import tkinter.font as tkfont


def resize_img(img, div_times_by):
    """
    Resizes an image to a given times_by
    """
    return img.resize((int(img.size[0] / div_times_by), int(img.size[1] / div_times_by)))


def convert_to_black_and_white(img, sensitivity):
    """
    Converts an image to black and white using a given sensitivity
    """
    fn = lambda x: 255 if x > sensitivity else 0
    return img.convert('L').point(fn, mode='1')


def img_to_array(img):
    """
    Converts an image to a numpy array
    """
    return np.array(img)


def generate_img_for_nonogram(path, div_times_by, sensitivity=128, show_stages=False):
    """
    Generates an image for a nonogram
    """
    img = Image.open(path)
    if show_stages:
        _, img_arr = plt.subplots(1, 3)
        img_arr[0].imshow(img)
        img_arr[0].set_title('Original')
    img = resize_img(img, div_times_by)
    if show_stages:
        img_arr[1].imshow(img)
        img_arr[1].set_title('Resized')
    img = convert_to_black_and_white(img, sensitivity)
    if show_stages:
        img_arr[2].imshow(img)
        img_arr[2].set_title('Black and white')
        plt.show()

    img_array = img_to_array(img)
    print("Nonogram dimensions: ", img_array.shape)
    return img_to_array(img)


def two_dim_to_nonogram(x, y, save_path):
    """
    Converts two lists to a nonogram
    """
    nonogram_list = y + x
    nonogram_data = tabulate(nonogram_list, tablefmt="grid")
    text_size = get_printed_size(str(nonogram_data), ("", 15))
    img = Image.new('RGB', (int(text_size[0]/(len(x) + len(y))/2.35), int(text_size[0]/(len(y[0]))/1.9)), color='white')
    d = ImageDraw.Draw(img)
    d.text((20, 20), str(nonogram_data), fill=(0, 0, 0))
    img.save(save_path)


def get_printed_size(text, myfont):
    root = tk.Tk()
    font = tkfont.Font(family=myfont[0], size=myfont[1])
    return font.measure(text), font.metrics("linespace")
