# import pywhatkit as pw

# txt="""Python is a versatile and powerful programming language known for its simplicity and readability. 
# It empowers developers to create everything from simple scripts to complex machine learning applications."""

# #three parameters will be given
# """1. text
#    2. Name of the File which is Optional give or not
#    if not then by default it will make a .png file in your dir
#    3. Color"""
# pw.text_to_handwriting(txt,"te2ha.png",[0,0,138])
# pw.text_to_handwriting(txt,"te2ha.png",[255,0,0]) #for red colour text
# print(" END ")

#Using an alternative library
import cv2
import numpy as np
import random

# Define the text to convert
text = """Python is a versatile and powerful programming language known for its simplicity and readability.
It empowers developers to create everything from simple scripts to complex machine learning applications."""

# Create a blank canvas
canvas_height, canvas_width = 800, 1200
canvas = np.ones((canvas_height, canvas_width, 3), dtype="uint8") * 255

# Initialize text position
x, y = 50, 70
line_spacing = 40

# Define font styles
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
font_scale = 0.8
color = (0, 0, 138)  # Blue handwriting-like color
thickness = 1

# Draw each line
for line in text.split("\n"):
    # Random vertical jitter to simulate human writing
    y_jitter = random.randint(-5, 5)
    cv2.putText(canvas, line, (x, y + y_jitter), font, font_scale, color, thickness, cv2.LINE_AA)
    y += line_spacing

# Save the result as an image
output_file = "handwriting_simulation.png"
cv2.imwrite(output_file, canvas)
print(f"Handwriting-style image saved as {output_file}")

# Show the result
cv2.imshow("Handwriting Simulation", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

#alternative method for this install module :
#syntax : pip install opencv-python
