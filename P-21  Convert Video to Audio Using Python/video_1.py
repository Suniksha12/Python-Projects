import moviepy.editor

#using tkinter
from tkinter.filedialog import *

vid = askopenfilename()

video = moviepy.editor.VideoFileClip(vid)

aud = video.audio

aud.write_audiofile("demo.mp3")

print("---END--")