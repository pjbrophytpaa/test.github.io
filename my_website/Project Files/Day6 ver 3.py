import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path
import PIL.ImageDraw
import numpy as np  # "as" lets us use standard abbreviations


  # Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
 # Build an absolute filename from directory + filename
filename = os.path.join(directory, 'scott.png')
orig = PIL.Image.open(filename)
filename = os.path.join(directory, 'scott_final.png')
img = PIL.Image.open(filename)



#stretch the beard
box_beard = (300,159,366,180) #grab the beard
region_beard = img.crop(box_beard) #crop it
#region_beard = region_beard.resize(40,80)
new_box_beard = (300,179,366,200)
img.paste(region_beard,new_box_beard)
new_box_beard = (300,199,366,220)
img.paste(region_beard,new_box_beard)
new_box_beard = (300,219,366,240)
img.paste(region_beard,new_box_beard)
new_box_beard = (300,239,366,260)
img.paste(region_beard,new_box_beard)
new_box_beard = (300,259,366,280)
img.paste(region_beard,new_box_beard)
new_box_beard = (300,279,366,300)
img.paste(region_beard,new_box_beard)
new_box_beard = (300,299,366,320)
img.paste(region_beard,new_box_beard)
new_box_beard = (300,319,366,340)
img.paste(region_beard,new_box_beard)
new_box_beard = (300,339,366,360)
img.paste(region_beard,new_box_beard)


#flip the image left/right
img = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
img = img.rotate(45)


'''Show the image data'''
  # Create figure with 2 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(orig, interpolation='none')
  # Show the figure on the screen
ax[1].imshow(img, interpolation='none')
fig.show()
