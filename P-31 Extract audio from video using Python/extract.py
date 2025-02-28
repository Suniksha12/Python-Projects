from moviepy.editor import *

# clip1 = VideoFileClip("test1.mp4").subclip(0,20)
# clip1.audio.write_audiofile("test1.mp3")

# clip1 = VideoFileClip("test2.mp4").subclip(5,25)
# clip1.audio.write_audiofile("test2.mp3")

# clip1 = VideoFileClip("test1.mp4").subclip(0,20)
# clip1 = clip1.without_audio()
# clip1.write_videofile("test_w1.mp4")

video_file = VideoFileClip("test_w1.mp4")
audio_file = AudioFileClip("test2.mp3")

final_video = video_file.set_audio(audio_file)
final_video.write_videofile("test_new1.mp4")