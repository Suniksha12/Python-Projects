from moviepy.editor import *

clip = VideoFileClip("test1.mp4").subclip(00,10)

clip= clip.margin(60)
clip.write_videofile("new_margin.mp4")

# clip.save_frame("test1.jpg",t=10)