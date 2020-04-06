from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import time
from random import randint

# proxies = ['115.171.85.114:9000',
# '114.31.20.2:8080',
# '114.238.46.29:21942',
# '115.221.209.194:9999',
# '146.196.120.138:52037',
# '140.238.52.254:3128',
# '140.82.61.93:8080',
# '144.217.163.138:8080']

# username = 'ramsuspect'
# emailOrPhone = 'ramsuspect@fft-mail.com'
# fullName = 'ram'
# password = 'qwerty123456'
ASSET = 'asset/'

with open(ASSET+'proxy.txt', 'r') as file:
	proxies = file.readlines()


opened = False
while not opened:
	proxy = proxies[randint(0,len(proxies)-1)]
	if proxy[:-1] == ' ':
		proxy = proxy[0:-2]
	firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
	firefox_capabilities['marionette'] = True

	firefox_capabilities['proxy'] = {
	    "proxyType": "MANUAL",
	    "httpProxy": proxy,
	    "ftpProxy": proxy,
	    "sslProxy": proxy
	}
	driver = webdriver.Firefox(capabilities=firefox_capabilities)
	try:
		# driver.get('https://httpbin.org/ip')
		print(proxy)
		driver.get('https://instagram.com/accounts/emailsignup/')
		try:
			inputElement = driver.find_element_by_name('emailOrPhone')
			opened = True
		except NoSuchElementException:
			print('error, trying another proxy')
			driver.close()
	except WebDriverException:
		print(proxy+' failed. Trying another proxy')
		driver.close()



# driver.get('https://www.instagram.com/accounts/emailsignup/')
# inputElement = driver.find_element_by_name('emailOrPhone')
# inputElement.send_keys(emailOrPhone)

# inputElement = driver.find_element_by_name('fullName')
# inputElement.send_keys(fullName)

# inputElement = driver.find_element_by_name('username')
# inputElement.send_keys(username)

# inputElement = driver.find_element_by_name('password')
# inputElement.send_keys(password)


# button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button')
# button.click()

# time.sleep(2)
# driver.close()