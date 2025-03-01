from moviepy.editor import *

clip1 = VideoFileClip("test1.mp4").subclip(5,15)
clip2 = VideoFileClip("test2.mp4").subclip(10,20)

clip2 = clip2.set_position((45,150))

final_video = concatenate_videoclips([clip1,clip2])

final_video.write_videofile("new_test.mp4")

#final video will be created but it will take some time wait for it.