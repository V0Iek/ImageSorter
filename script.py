import os

from PIL import Image
from PIL.ExifTags import TAGS

files = []

for file in os.listdir():
    if file.endswith(".jpg"):
        files.append(file)

for file in files:
    image = Image.open(file)
    exifdata = image.getexif()

    date = exifdata.get(306)
    date = date[:10]

    #print("-----", file, "-----")
    #print("Date: ", date)

    if not os.path.isdir(date):
        os.mkdir(os.path.join(os.getcwd(), date))

    source = os.path.join(os.getcwd(), file)
    dest = os.path.join(os.path.join(os.getcwd(), date), file)

    os.rename(source, dest)
