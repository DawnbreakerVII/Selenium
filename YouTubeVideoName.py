from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(2)
Entry= driver.find_element(By.XPATH,"//input[@id='search']")
Entry.send_keys("Title Name")    # The title by which you want to search the video 
Entry.send_keys(Keys.ENTER)
time.sleep(2)                    # Adjust according to internet speed
loopCounter = 0
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    if loopCounter > 7: 
        break
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(3)

    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if last_height == new_height:  
        break
    last_height = new_height
    loopCounter+=1         
time.sleep(3)
video = driver.find_element(By.XPATH,"//yt-formatted-string[.='Video Name']") # Enter the video name
video.click()
input("Press ENTER to exit\n")
