from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

bot = webdriver.Chrome('.\chromedriver.exe')

bot.get('https://www.facebook.com/')
time.sleep(15)
bot.find_element_by_id('email').send_keys('****@***.com')
bot.find_element_by_id('pass').send_keys('****')
bot.find_element_by_id('pass').send_keys(Keys.RETURN)
bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/a/div').click()
time.sleep(5)
pyautogui.press('s')
time.sleep(1)
pyautogui.press('l')
time.sleep(1)
pyautogui.press('enter')

