"""
Created on Mon Oct 21 13:35:05 2019

@author: serpil üstebay
email: serpil.ustebay@medeniyet.edu.tr

This program was written to group the pictures on the computer.
All images taken on different dates in the given directory are copied to the user-defined 'target' directory.
Copying is categorized according to the year and month of the image. For example:

source directory:
    Image00.jpeg      {is taken at 2017:10:12}
    Image012.jpg      {is taken at 2019:08:30}
    Image0121856.JPG  {is taken at 2019:07:30}

after executing the code

target directory:
    2019:
        08:
            Image012.jpg
        07:
            Image0121856.JPG
    2017:
        10:
            Image00.jpeg
"""

try:
    import os
    import shutil
    from PIL import Image
except ImportError as err:
    exit(err)


def organizeImagesDirectories(source, target):
    if os.path.isdir(source):
        os.chdir(source)
        for root, directories, files in os.walk(source):
            for file in files:
                extension = os.path.splitext(file)[
                    1]  # we try to get file extension. Some file extensions can be uppercase, lower case or just first capital is upper.
                if extension.lower() in ['.jpg',
                                         '.jpeg']:  # After convert file extension to the lowercase, I checked is it jpg oe jpeg file
                    try:
                        img = Image.open(file)
                        exif_data = img._getexif()
                        date = exif_data[306].split(":")  # extract picture taken date and split it according to ':'.
                        new_path = target + '/' + str(date[0]) + "/" + str(
                            date[1])  # new path  target+ image_taken_YEAR+image_taken_MONTH
                    except TypeError:
                        print("No EXIF date Information found for file:" + file)
                    if not os.path.exists(new_path):
                        # create new directory under target directory
                        os.makedirs(new_path)
                    shutil.copy2(root + '/' + file, new_path)
    else:
        print('Error: Source directory is wrong. Please check source directory')


if __name__ == '__main__':
    source = 'C:\\images'  # this is for images directory which you want to organize
    target = 'C:\\organizedImagesDirectory'  # Organized images will be copied to target directory

    organizeImagesDirectories(source, target)
