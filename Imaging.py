import string
import Image
import ImageFilter
import ImageEnhance
import ImageOps
import ImageDraw
import ImageFont


def contrast(image):
    """
    This function takes an image object as a parameter and applies contrast to it by making use of the ImageEnhance
    module. Degree is requested from raw_input(). It then returns this image object.
    """
    degree = float(raw_input("Please enter a number that represents the degree of contrast that you would like.\n" +
                             "Value must lie between 0.0 and 1.0 to decrease the contrast, or be greater than 1.0 to " +
                             "increase.\n"))
    enhancer = ImageEnhance.Contrast(im)
    out = enhancer.enhance(degree)
    return out


def brightness(image):
    """
    This function takes an image object as a parameter and applies brightness to it by making use of the ImageEnhance
    module. Degree is requested from raw_input(). It then returns this image object.
    """
    degree = float(raw_input("Please enter a number that represents the degree of brightness that you would like.\n" +
                             "Value must lie between 0.0 and 1.0 to decrease the brightness, or be greater than 1.0 " +
                             "to increase.\n"))
    enhancer = ImageEnhance.Contrast(im)
    out = enhancer.enhance(degree)
    return out


def colour(image):
    """
    This function takes an image object as a parameter and applies contrast from it by making use of the ImageEnhance
    module. Degree is requested from raw_input(). It then returns this image object.
    """
    degree = float(raw_input("Please enter a number that represents the saturation of colour you would like.\n" +
                             "Value must lie between 0.0 and 1.0 to decrease the colour saturation and be greater " +
                             "than 1.0 to increase.\n"))
    enhancer = ImageEnhance.Color(im)
    out = enhancer.enhance(degree)
    return out


def negative(image):
    """
    This function takes an image object as a parameter and inverts the colours by making use of the ImageOps module.
    It then returns this image object.
    """
    out = ImageOps.invert(image)
    return out


def emboss(image):
    """
    This function takes an image object as a parameter and applies embossing to it by making use of the ImageFilter
    module. It then returns this image object.
    """
    out = im.filter(ImageFilter.EMBOSS)
    return out


def sharpen(image):
    """
    This function takes an image object as a parameter and sharpens the image by making use of the ImageOps module.
    It then returns this image object.
    """
    while True:
        degree = float(raw_input("Please enter a number that represents the degree of sharpness that you would like.\n" +
                                 "Value must be greater than or equal to 2.0.\n"))
        if degree >= 2.0:
            enhancer = ImageEnhance.Sharpness(im)
            out = enhancer.enhance(degree)
            return out
        else:
            print "You entered a value which is out of range."
    

def soften(image):
    """
    This function takes an image object as a parameter and softens the image by making use of the ImageOps module.
    It then returns this image object.
    """
    while True:
        degree = float(raw_input("Please enter a number that represents the degree of softness that you would like.\n" +
                                     "Value must lie between 0.0 and 1.0.\n"))
        if degree > 0 and degree <= 1.0:
            enhancer = ImageEnhance.Sharpness(im)
            out = enhancer.enhance(degree)
            return out
        else:
            print "You entered a value which is out of range."


def blur(image):
    """
    This function takes an image object as a parameter and applies blurring to it by making use of the ImageFilter
    module. It then returns this image object.
    """
    out = im.filter(ImageFilter.BLUR)
    return out


def rotate(image):
    """
    This function takes an image object as a parameter and applies rotation to it by making use of the Image module.
    It then returns this image object.
    """
    while True:
        degree = float(raw_input("Please enter a number that represents the degree of rotation that you would like.\n" +
                                 "Value must lie between -360 and 360 degrees.\n"))
        if degree >= -360.0 and degree <= 360.0:
            out = im.rotate(degree)
            return out
        else:
            print "You entered a value which is out of range."


def v_flip(image):
    """
    This function takes an image object as a parameter and flips it vertically by making use of the ImageOps module.
    It then returns this image object.
    """
    out = ImageOps.flip(image)
    return out


def h_flip(image):
    """
    This function takes an image object as a parameter and flips it horizontally by making use of the ImageOps module.
    It then returns this image object.
    """
    out = ImageOps.mirror(image)
    return out


def resize(image):
    """
    This function takes an image object as a parameter and resizes it by making use of the Image module. Any cropping
    is performed from the centre of the image outwards. It then returns this image object.
    """
    width = int(raw_input("How many pixels wide should the image be?\n"))
    length = int(raw_input("How many pixels long should the image be?\n"))
    out = image.resize((width, length))
    return out


def chuck(image):
    """
    This function takes an image object as a parameter and splits the image into RGB bands by making use of the Image
    module. It then processes certain bands and rebuilds a new multiband image. It then returns this image object.
    """
    awesomeness = raw_input("How much awesomeness?\n Please enter a value between 0.0 and 250.0")
    im = image.convert("RGB")                                           # Convert to compatible image
    source = im.split()                                                 # Split into RGB colour bands
    R, G, B = 0, 1, 2
    mask = source[R].point(lambda i: i < 100)                           # Select regions where red is less than 100
    out = source[G].point(lambda i: i * 0.7)                            # Process the green band
    source[G].paste(out, None, mask)                                    # Paste processed band back where red was < 100
    im = Image.merge(im.mode, source)                                   # Build new multiband image
    im = im.point(lambda i:i < int(awesomeness) and 255)
    print "Chuck was here"
    return im


def add_text(image):
    """
    This function takes an image object as a parameter and adds text to it using ImageDraw and ImageFont modules. It
    then adds the text to the image and returns it.
    """
    font = ""
    font_color = ""

    text_to_add = raw_input("Enter some text you would like to add.\n")
    x = int(raw_input("Enter the x-coordinate for the text.\n"))
    y = int(raw_input("Enter the y-coordinate for the text.\n"))

    while True:
        user_font = raw_input("Would you like to use Arial, Times New Roman or Verdana?\nEnter A, T or V.\n")
        user_size = int(raw_input("What size font would you like to use?\n"))
        user_color = (raw_input("What colour font would you like to use?\nBl=Blue, B=Black, R=Red, W=White"))
        if user_color == "Bl":
            font_color = "blue"
        elif user_color == "B":
            font_color = "black"
        elif user_color == "R":
            font_color = "red"
        elif user_color == "W":
            font_color = "white"
        else:
            print "Invalid choice. Changing to default."
            font_color = "black"

        if user_font == "A" or "a":
            font = ImageFont.truetype('arial.ttf',user_size)
            break
        elif user_font == "T" or "t":
            font = ImageFont.truetype('times.ttf',user_size)
            break
        elif user_font == "V" or "v":
            font = ImageFont.truetype('verdana.ttf',user_size)
            break

    d = ImageDraw.Draw(image)

    d.text((x,y),text_to_add, font=font, fill=font_color) #should draw the string
    return im


print "----------------------------------------------------------------------------"
print string.center("Welcome to the Python Image Editing Application", 76)
print "----------------------------------------------------------------------------"

user_input = ""
out = ""
image_file = ""

while True:                                                             # Loop to act as sentinel for fetching a file
    try:
        image_file = raw_input("Please type in the name of the file that you would like to use.\n")
        im = Image.open(image_file)
        im.show()
        break
    except IOError:                                                     # Catching file errors
        print "ERROR! Incorrect filename or invalid file type."

while user_input != "Q":                                                # Loop to act as sentinel for entire application
    print "----------------------------------------------------------------------------"
    print string.center("MENU", 76)                                     # Some pretty GUI for a menu
    print "----------------------------------------------------------------------------"
    print ("\t\t\t\t1.\tContrast\n" + "\t\t\t\t2.\tBrightness\n" + "\t\t\t\t3.\tColour Saturation\n" +
           "\t\t\t\t4.\tNegative\n" + "\t\t\t\t5.\tEmboss\n" + "\t\t\t\t6.\tSharpen\n" + "\t\t\t\t7.\tSoften\n" +
           "\t\t\t\t8.\tBlur\n" + "\t\t\t\t9.\tRotate\n" + "\t\t\t\t10.\tFlip Vertically\n" +
           "\t\t\t\t11.\tFlip Horizontally\n" + "\t\t\t\t12.\tResize\n" + "\t\t\t\t13.\tDo Something Awesome\n" +
           "\t\t\t\t14.\tAdd Text\n" + "\t\t\t\tQ.\tQuit\n")
    print "----------------------------------------------------------------------------"
    user_input = raw_input("What would you like to do with the image?\n")

    try:
        if user_input == "Q":                                           # Call actions or functions for user options
            print "You chose to exit. Exiting now..."
            print "----------------------------------------------------------------------------"
            break
        elif user_input == "1":
            out = contrast(im)
        elif user_input == "2":
            out = brightness(im)
        elif user_input == "3":
            out = colour(im)
        elif user_input == "4":
            out = negative(im)
        elif user_input == "5":
            out = emboss(im)
        elif user_input == "6":
            out = sharpen(im)
        elif user_input == "7":
            out = soften(im)
        elif user_input == "8":
            out = blur(im)
        elif user_input == "9":
            out = rotate(im)
        elif user_input == "10":
            out = v_flip(im)
        elif user_input == "11":
            out = h_flip(im)
        elif user_input == "12":
            out = resize(im)
        elif user_input == "13":
            out = chuck(im)
        elif user_input == "14":
            out = add_text(im)
        else:
            print "FATAL ERROR! You entered an invalid option."         # Controlling for invalid menu options
            break
    except ValueError:                                                  # Handling value errors raised by functions
        print "ERROR! Only use numbers."
    print "Editing image..."
    out.show()                                                          # Display image once function has edited it
    undo = raw_input("Would you like to save your changes? (Y/N)\n")    # Allow user option for saving file
    if undo == "N":
        print "Restoring original image..."                             # File is unchanged and unsaved
    elif undo == "Y":
        while True:
            im = out
            save_file = raw_input("What would you like to save your image as?\n")
            if save_file == image_file:                                 # Check for overwriting
                sure = raw_input("Are you sure you want to overwrite the file " + save_file + "? (Y/N)\n")
                if sure == "Y":
                    try:
                        im.save(save_file)                              # Save file if user is certain
                        image_file = save_file
                        print "Changes saved."
                        break
                    except IOError:                                     # Handle file errors
                        print "ERROR! There was a problem saving the file."
                    except KeyError:                                    # Handle key errors for file extensions
                        print "ERROR! You failed to save the file with a valid extension."
                elif sure == "N":                                       # File is unchanged and unsaved but user is
                    pass                                                # presented with another opportunity to save
                else:
                    print "ERROR! You entered an invalid option."       # Controlling for invalid menu options
            else:
                try:                                                    # Saving if not overwriting
                    im.save(save_file)
                    image_file = save_file                              # Save file
                    print "Changes saved."
                    break
                except IOError:                                         # Handle file and extension errors
                    print "ERROR! There was a problem saving the file."
                except KeyError:
                        print "ERROR! You failed to save the file with a valid extension."