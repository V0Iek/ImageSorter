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

    #for tagid in exifdata:
    #    tagname = TAGS.get(tagid, tagid)
    #    value = exifdata.get(tagid)

    #    if "Date" in tagname:
    #        print(tagid)
    #        print(value)

    date = exifdata.get(306)

    date = date[:10]

    print("-----", file, "-----")
    print("Date: ", date)
