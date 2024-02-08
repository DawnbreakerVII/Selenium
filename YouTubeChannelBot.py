from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")

time.sleep(5)
Giris= driver.find_element(By.XPATH,"//input[@id='search']")
Giris.send_keys("Channel name ") # Channel name
Giris.send_keys(Keys.ENTER)
time.sleep(5)
Vishanti = driver.find_element(By.XPATH,"//*[@id='channel-title']")
Vishanti.click()
time.sleep(5)
Videolar = driver.find_element(By.XPATH,"//tp-yt-paper-tab[2]/div[@class='tab-content style-scope tp-yt-paper-tab']")
Videolar.click()
time.sleep(5)
son = driver.find_element(By.XPATH,"//yt-formatted-string[.='Video name']") # Video name
son.click()
time.sleep(5)
input("Press ENTER to exit\n")
