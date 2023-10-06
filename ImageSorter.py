#!/usr/bin/env python3

import os

from PIL import Image
from PIL.ExifTags import TAGS

# Create list with .jpg files in current dir
files = []

for file in os.listdir():
    if file.endswith(".jpg"):
        files.append(file)


for file in files:
    # Get metadata from file
    image = Image.open(file)
    exifdata = image.getexif()

    # Get data from metadata
    date = exifdata.get(306)
    date = date[:10]
    date = date[8:] + "." + date[5:7] + "." + date[:4]

    # Create dir with date if not exist
    if not os.path.isdir(date):
        os.mkdir(os.path.join(os.getcwd(), date))

    # Move image to folder with its date
    source = os.path.join(os.getcwd(), file)
    dest = os.path.join(os.path.join(os.getcwd(), date), file)

    os.rename(source, dest)
