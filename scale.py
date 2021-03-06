# -*- coding:utf-8  -*-
'''
image scale resize
'''

from PIL import Image
import glob


def process_image(filename, mwidth=1500, mheight=1500):
    image = Image.open(filename)
    w, h = image.size
    if w <= mwidth and h <= mheight:
        print(filename, 'is OK.')
        return
    if (1.0 * w / mwidth) > (1.0 * h / mheight):
        scale = 1.0 * w / mwidth
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)

    else:
        scale = 1.0 * h / mheight
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    print("resize image" + filename)
    new_im.save('new-' + filename)
    new_im.close()


for infile in glob.glob("*.jpg"):
    # file, ext = os.path.splitext(infile)
    print(infile)
    process_image(infile)
