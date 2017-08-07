from icrawler.builtin  import GoogleImageCrawler
import os
import sys
import subprocess
from PIL import Image

# Easy coaleasce function
def coalesce(*arg):
  for el in arg:
    if el is not None:
      return el
  return None

# Get label to associate (also used as foldername)
label = sys.argv[1]

# Get the search term to crawl against or default to label
searchTerm = label

# Set the directory where we should place our images from crawler
imageDirectory = 'Image_Data/' + label


# Check if the directory already exists
if not os.path.exists(imageDirectory):
        # Directory doesnt exist so we need to create it
        os.mkdir(imageDirectory)

# Use our crawler
googleCrawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                            storage={'root_dir': imageDirectory})
googleCrawler.crawl(
    keyword=searchTerm, max_num=1000,
    date_min=None, date_max=None,
    min_size=(200,200), max_size=None
    )

# Check that the file is a jpeg and that it is not corrupt junk
def is_jpg(filename):
    try:
        i=Image.open(filename)
        return i.format =='JPEG'
    except IOError:
        return False

for root, dirs, files in os.walk(imageDirectory):
		for currentFile in files:
			ext = '.jpg'
			imagePath =  root + '/' + currentFile
			print(imagePath)
			if (not is_jpg(imagePath)):
			 	print('not jpg')
			 	os.remove(os.path.join(root, currentFile))