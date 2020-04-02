from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

mail = 'paviparvathi123@hotmail.com'
password = 'qwerty123456'
driver = webdriver.Firefox()
driver.get('https://www.instagram.com')

#paths
path_profile = '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/span'
path_profile_setting = '/html/body/div[1]/section/main/div/header/section/div[1]/div/button'
path_privacy = '/html/body/div[4]/div/div/div/button[5]'
path_privacy_chkbx = '//*[@id="f1c9e2a4ed7b948"]'

inElement = driver.find_element_by_name('username')
inElement.send_keys(mail)
inElement = driver.find_element_by_name('password')
inElement.send_keys(password)



login_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button').send_keys(Keys.RETURN)
sleep(2)
try:
	not_now = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
except NoSuchElementException:
	pass

def gotoprofile():
	profile = driver.find_element_by_xpath(path_profile)
	profile.click()
	sleep(2)

profile_setting = driver.find_element_by_xpath(path_profile_setting)
profile_setting.click()
sleep(2)

privacy = driver.find_element_by_xpath(path_privacy)
privacy.click()
sleep(2)

privacy_chkbx = driver.find_element_by_xpath(path_privacy_chkbx)
privacy_chkbx.click()
sleep(5)


# driver.get('https://www.instagram.com/p/B-ZvdXZha17/?utm_source=ig_web_copy_link')