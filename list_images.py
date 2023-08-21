import os
import re
import sys

DIR_IMAGES = './images'

def get (dir=DIR_IMAGES):
    list_images = []

    for file in os.listdir(dir):
        if re.search('^\$mark_.+\.(png|jpg|jpeg)$', file):
            list_images.append(os.path.join(dir, file))

    return list_images

if __name__ == '__main__':
    print(get())
    sys.exit()
