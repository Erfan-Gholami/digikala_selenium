from selenium import webdriver
from time import sleep
import random

driver = webdriver.Firefox(executable_path = 'C:/Program Files/Firefox Developer Edition/geckodriver.exe')

email = "jerald1376@gmail.com"
password = "J?KWCnyR"

getdriver = ("https://digikala.com")

driver.get(getdriver)

def login():
    driver.find_element_by_xpath("//*[@class='c-header__btn-login o-tooltip']").click()
    sleep(3)
    email_area = driver.find_element_by_name('login[email_phone]')
    email_area.send_keys(email)
    driver.find_element_by_xpath('//*[@id="loginForm"]/button').click()
    sleep(3)
    driver.find_element_by_name('login[password]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="authForm"]/button').click()
    sleep(3)
    driver.find_element_by_xpath("//*[@class='c-header__btn-profile js-dropdown-toggle']").click()

login()

