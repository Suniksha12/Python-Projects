from moviepy.editor import *

clip = VideoFileClip("demo1.mp4").subclip(0,10)

txt_clip = TextClip("Whoosh Tech",fontsize=50, color="Black")

txt_clip = txt_clip.set_position('center').set_duration(10)

video = CompositeVideoClip([clip,txt_clip])

video.write_videofile("test.mp4")