from moviepy.editor import *
from datetime import datetime

def create_video(audio_filename, screen_video_filename,log):
    audio = AudioFileClip(audio_filename)
    video_file = VideoFileClip(screen_video_filename)

    video = CompositeVideoClip([video_file]).set_audio(audio)
    video.write_videofile("video_audio.avi", codec='libx264', fps=12)
    log.write("Paste video and audio at {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))