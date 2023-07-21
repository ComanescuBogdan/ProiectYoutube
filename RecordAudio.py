import shutil

import pyaudio
import wave
from _datetime import datetime


def audio(log):

    log.write("Started audio recording at {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    # the file name output you want to record into
    filename = "out.wav"
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 1
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = 15
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        # if you want to hear your voice while recording
        # stream.write(data)
        frames.append(data)
    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    log.write("Ended audio recording at {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # save audio file
    total, used, free = shutil.disk_usage("/")
    required_size = len(frames) * chunk
    if free < required_size:
        log.write("Not enough disk space. Audio recording not saved.\n")
    else:
        # open the file in 'write bytes' mode
        wf = wave.open(filename, "wb")
        # set the channels
        wf.setnchannels(channels)
        # set the sample format
        wf.setsampwidth(p.get_sample_size(FORMAT))
        # set the sample rate
        wf.setframerate(sample_rate)
        # write the frames as bytes
        wf.writeframes(b"".join(frames))
        # close the file
        wf.close()
        log.write("Audio recording saved.\n")


##########################################################

# import soundcard as sc
# import soundfile as sf
#
# OUTPUT_FILE_NAME = "out.wav"
# SAMPLE_RATE = 48000
# RECORD_SEC = 5
#
# def audio():
#     with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(
#             samplerate=SAMPLE_RATE) as mic:
#         # record audio with loopback from default speaker.
#         data = mic.record(numframes=SAMPLE_RATE * RECORD_SEC)
#
#         # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
#         sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
#########################################################################################
