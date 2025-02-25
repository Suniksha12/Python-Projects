from moviepy.editor import *

#add your path below
video = VideoFileClip("").subclip(00,5)
video.write_gif("test1.gif")