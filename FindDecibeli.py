
import moviepy.editor as mp
import numpy as np
import soundfile as sf

def measure_audio_level(video_file, audio_file, output_file):
    # Extract audio from the video file
    video = mp.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)

    # Load the audio file and calculate the dB level
    data, sample_rate = sf.read(audio_file)
    rms = np.sqrt(np.mean(data ** 2))
    db_level = 20 * np.log10(rms)

    output_file.write("Sound level: {} dB\n".format(db_level))

    # Remove the temporary audio file
    audio.close()
    video.close()

