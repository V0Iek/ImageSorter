import os

files = []

for file in os.listdir():
    if file.endswith(".png"):
        print(file, " is image")
        files.append(file)
    else:
        print(file, " isn't image")

print(files)
