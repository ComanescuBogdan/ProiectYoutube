import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


import VerifyInternetConnection as vInternet
import OpenYouTube as youtube
import OpenVideo as video


options = webdriver.FirefoxOptions()
log = open("LogFile.log","w")

if vInternet.conexiune():
    log.write("Urmeaza deschiderea paginii web")

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    driver.implicitly_wait(120)
    wait = WebDriverWait(driver, 10)


    youtube.open(driver,wait,log)
    time.sleep(2)
    video.open(driver,wait,log)
    time.sleep(1)
    video.play(driver,wait,log)



else:
    log.write("Nu avem conexiune la internet")

