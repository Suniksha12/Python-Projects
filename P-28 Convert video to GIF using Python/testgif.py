from moviepy.editor import *

#add your path below
# video = VideoFileClip("").subclip(00,5)
# video.write_gif("test1.gif")

#if we want to make the GIF rotate for which we will be needed 
video = VideoFileClip("").subclip(00,5).rotate(180)
video.write_gif("test2.gif")