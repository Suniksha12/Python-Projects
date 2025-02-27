from moviepy.editor import *

clip_1 = VideoFileClip("demo1.mp4").subclip(0,10)
clip_2 = VideoFileClip("demo2.mp4").subclip(10,20)
clip_3 = VideoFileClip("demo3.mp4").subclip(00,10)
clip_4 = VideoFileClip("demo4.mp4").subclip(00,10)

