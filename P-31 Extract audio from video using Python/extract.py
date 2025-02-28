from moviepy.editor import *

# clip1 = VideoFileClip("test1.mp4").subclip(0,20)
# clip1.audio.write_audiofile("test1.mp3")

clip1 = VideoFileClip("test2.mp4").subclip(5,25)
clip1.audio.write_audiofile("test2.mp3")