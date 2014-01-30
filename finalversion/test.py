import glob
import os

images = glob.glob('../data/*.png')

def stripEnding(image):
	index = image.find('.')
	return image[:index]

for image in images:
	print stripEnding(os.path.basename(image))
