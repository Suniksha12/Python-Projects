from moviepy.editor import *

clip = VideoFileClip("test1.mp4")

clip.save_frame("test1.jpg",t=10)