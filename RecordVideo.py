import shutil

import cv2
import numpy as np
import pyautogui
from _datetime import datetime


def record(log):

    log.write("Started video recording at {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    # display screen resolution, get it using pyautogui itself
    SCREEN_SIZE = tuple(pyautogui.size())
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # frames per second
    fps = 12.0
    # create the video write object
    out = cv2.VideoWriter("video.avi", fourcc, fps, (SCREEN_SIZE))
    # the time you want to record in seconds
    record_seconds = 15

    required_size = int(record_seconds * fps) * SCREEN_SIZE[0] * SCREEN_SIZE[1] * 3  # 3 channels for BGR color

    # Check available disk space
    total, used, free = shutil.disk_usage("/")
    if free < required_size:
        log.write("Not enough disk space. Video recording not saved.\n")
    else:
        for i in range(int(record_seconds * fps)):
            # make a screenshot
            img = pyautogui.screenshot()
            # convert these pixels to a proper numpy array to work with OpenCV
            frame = np.array(img)
            # convert colors from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # write the frame
            out.write(frame)# de facut verfi
            # if the user clicks q, it exits
            if cv2.waitKey(1) == ord("q"):
                break

    # make sure everything is closed when exited
    cv2.destroyAllWindows()
    out.release()
    log.write("Ended video recording at {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))



