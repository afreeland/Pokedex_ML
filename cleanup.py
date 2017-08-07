import os
import sys
import subprocess

# Set the directory where we should place our images from crawler
imageDirectory = 'Image_Data'

for root, dirs, files in os.walk(imageDirectory):
		for currentFile in files:
			ext = '.jpg'
			s = subprocess.getstatusoutput('file ' + currentFile)[1]
			print(s)
			if ((s.find('JPEG image data') == -1) or (not currentFile.lower().endswith(ext))):
				os.remove(os.path.join(root, currentFile))
