from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


import VerifyInternetConnection as vInternet
import OpenYouTube as youtube

options = webdriver.FirefoxOptions()
log = open("LogFile.log","w")

if vInternet.conexiune():
    log.write("Urmeaza deschiderea paginii web")

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    wait = WebDriverWait(driver, 10)

    youtube.open(driver,wait,log)
else:
    log.write("Nu avem conexiune la internet")







# driver.get('http://www.youtube.com')
# assert 'YouTube' in driver.title
# driver.implicitly_wait(20)

#
#
# reject_button = driver.find_element(By.XPATH,"/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
# reject_button.click()
# driver.implicitly_wait(20)

