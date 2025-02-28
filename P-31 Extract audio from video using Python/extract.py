from moviepy.editor import *

clip1 = VideoFileClip("test1.mp4").subclip(0,20)
clip1.audio.write_audiofile("test1.mp3")