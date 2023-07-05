from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def open(browser, wait,log):
    browser.get('http://www.youtube.com')


    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.write("Acesat {} la {}\n".format(browser.title, current_time))

    reject_text= "Reject the use of cookies and other data for the purposes described"

    try:
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@aria-label='{}']".format(reject_text))))
        reject_cookies_btn = browser.find_elements(By.XPATH, "//button[@aria-label='{}']".format(reject_text))
    except TimeoutException:
        return

    if len(reject_cookies_btn) == 0:
        log.write("Butonul de reject cookies nu a fost gasit!\n")
        browser.quit()
        raise SystemExit
    else:
        reject_cookies_btn = reject_cookies_btn[0]


    browser.execute_script("arguments[0].click()", reject_cookies_btn)
    log.write("Cookie-uri refuzate la {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

