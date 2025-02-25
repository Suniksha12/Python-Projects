# import pywhatkit as kit

# kit.image_to_ascii_art('C:/Users/sunik/OneDrive/Desktop/Python Projects/P-27 Image to ASCII Art using Python/WHOOSH.png',"ascii.txt")

#there is an another module through which we can make the ascii image for which again open your command prompt
#and install command : pip install ascii-magic

import ascii_magic

# Convert image to ASCII
output = ascii_magic.from_image(
    "C:/Users/sunik/OneDrive/Desktop/Python Projects/P-27 Image to ASCII Art using Python/WHOOSH.png"
)

# Print the ASCII output correctly
print(output.to_ascii())


