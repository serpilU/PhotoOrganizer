# PhotoOrganizer

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
||
||-------------2019:
|___________________08:
|_______________________Image012.jpg
        07:
            Image0121856.JPG
    2017:
        10:
            Image00.jpeg

