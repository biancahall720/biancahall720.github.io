# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    i = Image.open(filename)
    return img

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(img):
    img.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(img, filename):
    imsge.save(filename, "jpeg")

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):
    low_intensity = 182
    med_int = 364
    high_int = 540
    
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)





pix = im.getdata()

for pixel in pix:
    intensity = pixel[0]+pixel[1]+pixel[2]


    if (intensity < low)
elif(intensity > low and intensity < med):
