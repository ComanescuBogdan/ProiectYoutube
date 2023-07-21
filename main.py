import threading
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from VideoAudio import *
import VerifyInternetConnection as vInternet
import OpenYouTube as youtube
import OpenVideo as video
from RecordVideo import *
from RecordAudio import *
from FindDecibeli import *

options = webdriver.FirefoxOptions()
log = open("LogFile.log","w") # trebuie verificat
# trebuie inchis la final

def time_connected(log):
    start_time = time.time()
    while time.time() - start_time < 15:
        if not vInternet.conexiune():
            log.write("Internet connection failed at {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))) # verificare daca este valid
            break
        else:
            continue
    log.write("Connection was successful at {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


if vInternet.conexiune():
    log.write("Urmeaza deschiderea paginii web\n")

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)



    youtube.open_browser(driver,wait,log)
    time.sleep(2)
    video.open_video(driver,wait,log)
    time.sleep(1)
    video.play(driver,wait,log)


    video_thread = threading.Thread(target=record,args=(log,))
    audio_thread = threading.Thread(target=audio,args=(log,))
    connection_thread = threading.Thread(target=time_connected,args=(log,))

    video_thread.start()
    audio_thread.start()
    connection_thread.start()


    video_thread.join()
    audio_thread.join()
    connection_thread.join()


    create_video("out.wav","video.avi",log)

    measure_audio_level("out.wav",log)

    driver.close()


else:
    log.write("No internet connection\n")

