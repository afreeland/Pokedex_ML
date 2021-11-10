from icrawler.builtin import GoogleImageCrawler
import os
import sys
import string
import subprocess
import shutil
from PIL import Image

# Easy coaleasce function


def coalesce(*arg):
    for el in arg:
        if el is not None:
            return el
    return None

# Check that the file is an image and that it is not corrupt junk


def is_img(filename):
    try:
        i = Image.open(filename)
        return i.format == 'JPEG' or i.format == 'JPG' or i.format == 'PNG'
    except IOError:
        return False


print(sys.argv)
# Get label to associate (also used as foldername)
label = sys.argv[1]

# Get the search term to crawl against or default to label
searchTerm = label


imageTypes = [label, label + ' cards', label + ' plush']


for imageType in imageTypes:
    trimmedType = imageType.translate(str.maketrans('', '', string.whitespace))

    # Set the directory where we should place our images from crawler
    imageDirectory = 'Image_Data/' + trimmedType

    # Check if the directory already exists
    if not os.path.exists(imageDirectory):
        # Directory doesnt exist so we need to create it
        os.mkdir(imageDirectory)

    # Use our crawler
    googleCrawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                       storage={'root_dir': imageDirectory})
    googleCrawler.crawl(
        keyword=imageType, max_num=1000,
        min_size=(200, 200), max_size=None
    )

    for root, dirs, files in os.walk(imageDirectory):
        for currentFile in files:
            ext = '.jpg'
            imagePath = root + '/' + currentFile
            print(imagePath)
            if (not is_img(imagePath)):
                print('not jpg')
                os.remove(os.path.join(root, currentFile))
            else:
                # Only move files that are not from our original arg (ie: cards, plush)
                if imageType != label:
                    shutil.move(imagePath, './Image_Data/' +
                                label + '/' + trimmedType + "_" + currentFile)

    # Delete our extra folders once we moved all files into the primary folder
    if imageType != label:
        if os.path.exists(imageDirectory):
           # removing the file using the os.remove() method
            os.rmdir(imageDirectory)
