from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--dissable-popup-blocking")
chrome_options.add_argument(r"--user-data-dir=C:\Users\maxko\Desktop\bot")
chrome_options.add_argument("--profile-directory=Profile 1")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://nomada.margonem.pl/")

time.sleep(5)

exit_loop = False

while not exit_loop:
    try:
        element = driver.find_element(By.ID, "npc160694")

        time.sleep(2)

        element.click()

        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"{current_time}: kliknieto na potwora.")

        time.sleep(2)

        element.click()

        time.sleep(10)

        driver.get("https://www.margonem.pl/")

        time.sleep(300)

        driver.get("https://nomada.margonem.pl/")

        time.sleep(5)

    except NoSuchElementException:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"{current_time}: szukam")

        time.sleep(2)
