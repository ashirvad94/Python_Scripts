from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class twitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome('.\chromedriver.exe')

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        vUserName = bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input')
        vPassword = bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input')
        vUserName.send_keys(self.username)
        vPassword.send_keys(self.password)
        vPassword.send_keys(Keys.RETURN)
        time.sleep(5)
        bot.find_element_by_xpath('/html/body/div/div/div/div/header/div/div/div/div/div[2]/nav/a[2]/div').click()
        vSearch = bot.find_element_by_css_selector('#react-root > div > div > div > main > div > div > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-14lw9ot.r-my5ep6.r-rull8r.r-qklmqi.r-gtdqiz.r-ipm5af.r-1g40b8q > div.css-1dbjc4n.r-14lw9ot.r-136ojw6 > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1pi2tsx.r-1777fci > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-5f2r5o.r-zg41ew > div > div > div > form > div.css-1dbjc4n.r-1wbh5a2 > div > div > div.css-901oao.r-hkyrab.r-6koalj.r-16y2uox.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > input')

        vSearch.send_keys('****')
        vSearch.send_keys(Keys.RETURN)
       
vPass = twitterBot('****', '****')
vPass.login()

