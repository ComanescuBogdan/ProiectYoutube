import time

import numpy.random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from _datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait


def open_video(browser,wait,log):

    try:
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@id='{}']".format("thumbnail"))))
        videos = browser.find_elements(By.XPATH, "//yt-formatted-string[@id='video-title']")
    except:
        return


    if len(videos)>0:
        nr_random = numpy.random.randint(1,len(videos)-1)
        browser.execute_script("arguments[0].click()", videos[nr_random])
    else:
        log.write("Not video found!\n")



def play(browser,wait,log):


    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-large-play-button ytp-button']")))
        play_btn = browser.find_element(By.XPATH, "//button[@class='ytp-large-play-button ytp-button']")
        play_btn.click()
        log.write("Played video at {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    except TimeoutException:
        log.write("Play button doesn't exist!\n")
        return

    # time.sleep(6)

    try:
        skip_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-ad-skip-button ytp-button']")))
        if skip_button:
            skip_button.click()
            log.write("Skip button clicked at {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    except:
        log.write("Skip button doesn't exist!\n")

