from moviepy.editor import *

clip = VideoFileClip("test1.mp4")

clip.save_frame("test2.jpg",t=10)