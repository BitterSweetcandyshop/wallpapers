from PIL import Image
from os import listdir

path_to_download = "/home/bittersweet/Documents/unixporn_wallpapers/"
width = 2560
height = 1440


################################
count = 0
for image in listdir(path_to_download):
    try:
        img = Image.open(path_to_download + image)
        w, h = img.size
        if (w >= width) and (h >= height):
            print(str(w) + "x" + str(h) + "  " + image)
            count += 1
    except:
        pass

print("Total matching found: " + str(count))