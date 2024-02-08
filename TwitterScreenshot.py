from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("https://twitter.com/login")
time.sleep(2)
driver.maximize_window()
usernameInput = driver.find_element(By.XPATH,"//input[@name='text']")
time.sleep(2)
usernameInput.send_keys(username)
time.sleep(2)
button = driver.find_element(By.CSS_SELECTOR,"div:nth-of-type(6)")
button.click()
time.sleep(2)
passwordInput = driver.find_element(By.XPATH,"//input[@name='password']")
time.sleep(2)
passwordInput.send_keys(password)
time.sleep(2)
btnSubmit = driver.find_element(By.CSS_SELECTOR,".r-19yznuf")
btnSubmit.click()
time.sleep(5)
searchInput = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
searchInput.send_keys("Username") # Username
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
user = driver.find_element(By.XPATH, "//div[@class='css-175oi2r r-1awozwy r-18u37iz r-1wtj0ep']//div[@class='css-175oi2r r-1wbh5a2 r-dnmrzs r-1ny4l3l']/div[@class='css-175oi2r r-1wbh5a2 r-dnmrzs']//span[@class='css-1qaijid r-bcqeeo r-qvutc0 r-poiln3']")
user.click()
time.sleep(2) 
userAnswer = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/nav/div/div[2]/div/div[2]/a")
userAnswer.click()
tweet = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div/div/div[4]/div/div/article")
tweet.click()
driver.get_screenshot_as_file("tweet.png")
#searchInput.send_keys(Keys.ENTER)
input("Press ENTER to exit\n")

'''
    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        results = []

        list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")
        time.sleep(2)
        print("count: "+ str(len(list)))

        for i in list:
            results.append(i.text)

        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 5:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter+=1

            list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")
            time.sleep(2)
            print("count: "+ str(len(list)))

            for i in list:
                results.append(i.text)

        count = 1
        with open("tweets.txt","w",encoding="UTF-8") as file:
            for item in results:
                file.write(f"{count}-{item}\n")
                count+=1


        # count = 1
        # for item in results:            
        #     print(f"{count}-{item}")
        #     count+=1
        #     print("***********")

'''

#twitter = Twitter(username,password)
# login
#twitter.singIn()
#twitter.search("python")



    

