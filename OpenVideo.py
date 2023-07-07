import numpy.random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def open(browser,wait,log):

    try:
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@id='{}']".format("thumbnail"))))
        videos = browser.find_elements(By.XPATH, "//yt-formatted-string[@id='video-title']")
    except:
        return

    nr_random = numpy.random.randint(1,len(videos)-1)
    browser.execute_script("arguments[0].click()", videos[nr_random])




def play(browser,wait,log):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-large-play-button ytp-button']")))
        play_btn = browser.find_element(By.XPATH, "//button[@class='ytp-large-play-button ytp-button']")
        print("a mers")
        play_btn.click()
    except TimeoutException:
        print("Nu l am gasit")


    try:
        skip_button =  wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-ad-skip-button ytp-button']")))
        if skip_button:
            print("Am gasit skip buton")
            skip_button.click()
    except:
        print("Nu am gasit skip buton")
