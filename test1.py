from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

proxy = "165.227.77.10:3128"
username = 'ramsuspect'
emailOrPhone = 'ramsuspect@fft-mail.com'
fullName = 'ram'
password = 'qwerty123456'

firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True

firefox_capabilities['proxy'] = {
    "proxyType": "MANUAL",
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy
}

driver = webdriver.Firefox(capabilities=firefox_capabilities)

# driver.get('https://temp-mail.org/en/api/')

driver.get('https://www.instagram.com/accounts/emailsignup/')
inputElement = driver.find_element_by_name('emailOrPhone')
inputElement.send_keys(emailOrPhone)

inputElement = driver.find_element_by_name('fullName')
inputElement.send_keys(fullName)

inputElement = driver.find_element_by_name('username')
inputElement.send_keys(username)

inputElement = driver.find_element_by_name('password')
inputElement.send_keys(password)


button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button')
button.click()

# time.sleep(2)
# driver.close()