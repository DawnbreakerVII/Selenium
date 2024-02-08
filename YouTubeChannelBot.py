from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")

time.sleep(5)
entry driver.find_element(By.XPATH,"//input[@id='search']")
entry.send_keys("Channel name ") # Channel name
entry.send_keys(Keys.ENTER)
time.sleep(5)
Channel = driver.find_element(By.XPATH,"//*[@id='channel-title']")
Channel.click()
time.sleep(5)
Videos = driver.find_element(By.XPATH,"//tp-yt-paper-tab[2]/div[@class='tab-content style-scope tp-yt-paper-tab']")
Videos.click()
time.sleep(5)
video = driver.find_element(By.XPATH,"//yt-formatted-string[.='Video name']") # Video name
video.click()
time.sleep(5)
input("Press ENTER to exit\n")
