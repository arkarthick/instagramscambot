from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from random import randint
from details import dob
import asset.password as password

ASSET = 'asset/'

def login(username):
	#enter the username or mail and password
	try:
		sleep(3)
		inElement = driver.find_element_by_name('username')
		inElement.send_keys(username)
		inElement = driver.find_element_by_name('password')
		inElement.send_keys(password.password)
		inElement.send_keys(Keys.RETURN)
		# login_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button').send_keys(Keys.RETURN)
		# print('logged in')
		sleep(7)
		print('logged in as '+ username)
		try:
			not_now = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
			not_now.click()
			print('notification turned off')
			sleep(2)

		except NoSuchElementException:
			pass
	except NoSuchElementException:
		print('login failed')
	
	#goes to the profile area
	try:
		path_profile = '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span'
		profile = driver.find_element_by_xpath(path_profile)
	except NoSuchElementException:
		path_profile = '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/span'
		profile = driver.find_element_by_xpath(path_profile)

	try:
		profile.click()
		sleep(2)
	except NoSuchElementException:
		print('profile icon not found')

	#get the username
	global username_cap
	try:
		username_cap = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/h2').text
		# return username_cap
	except:
		username_cap = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/h2').text

	print(username_cap)
# def get_username():
# 	# global username_cap
# 	goto_profile_init()
	

def goto_profile():
	#redirect to the profile page
	driver.get('https://instagram.com/'+username_cap+'/')

def goto_editprofile():
	#press the edit profile icon in the profile page
	goto_profile()
	path_edit_profile = '/html/body/div[1]/section/main/div/header/section/div[1]/a/button'
	try:
		editprofile = driver.find_element_by_xpath(path_edit_profile)
		editprofile.click()
		sleep(1)
	except NoSuchElementException:
		print('edit profile btn not found')

def profilesetting():
	#press the setting icon in the profile page
	goto_profile()
	path_profile_set = '/html/body/div[1]/section/main/div/header/section/div[1]/div/button'
	try:
		profile_setting = driver.find_element_by_xpath(path_profile_set)
		profile_setting.click()
		sleep(2)
	except NoSuchElementException:
		print('profile setting not found')

def privacy_setting():
	# changes the privacy of the account
	profilesetting()
	path_privacy = '/html/body/div[4]/div/div/div/button[5]'
	path_privacy_chkbx = '/html/body/div[1]/section/main/div/article/main/section[1]/div/div/div/label/div'
	try:
		privacy = driver.find_element_by_xpath(path_privacy)
		privacy.click()
		sleep(5)
		try:
			privacy_chkbx = driver.find_element_by_xpath(path_privacy_chkbx)
			privacy_chkbx.click()
			print('Privacy of the account is changed')
			sleep(5)
			goto_profile()
		except:
			print('checkbox not found')
	except NoSuchElementException:
		print('privacy_setting failed')
		pass

def generate_bio(bio_data):
	date_of_birth = dob()
	if date_of_birth != None:
		bio = [bio_data +'\n' + date_of_birth ,  date_of_birth +'\n' + bio_data ]
		return bio[randint(0,1)]
	else:
		return bio_data

def set_bio():
	bio_data = 'I’m not smart; I just wear glasses.'
	goto_editprofile()
	bio_data = generate_bio(bio_data)
	path_bio = '//*[@id="pepBio"]'
	try:
		bio = driver.find_element_by_xpath(path_bio)
		bio.send_keys(bio_data)
		submit = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[11]/div/div/button[1]')
		submit.click()
		sleep(4)
		print('bio updated')
		goto_profile()
	except NoSuchElementException:
		print('set_bio operation failed')

def logout():
	# logout from the account
	profilesetting()
	path_logout = '/html/body/div[4]/div/div/div/button[9]'
	logout = driver.find_element_by_xpath(path_logout).click()
	sleep(2)
	print('logged out')
	print('\n\n')
	try:
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[1]').click()
	except NoSuchElementException:
		pass
	sleep(2)

def like(link_id):
	url = 'https://www.instagram.com/p/'
	driver.get(url+link_id+'/')
	sleep(5)
	try:
		driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button').click()
		sleep(6)
		print('liked')
		sleep(5)
		goto_profile()
	except Exception as e:
		print('like btn not found')

def change_profile():
	pass

def follow(username):
	url = 'https://www.instagram.com/'+username+'/'
	driver.get(url)
	sleep(2)
	follow_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
	follow_btn.click()
	sleep(10)

def run(user_id, link_id_list, usernames):
	driver.get('https://www.instagram.com')
	for user in user_id:
		login(user)
		# username = get_username()
		# get_username()
		with open(ASSET+'username.txt', 'a') as f:
			f.write(username_cap+'\n')
		# privacy_setting()
		# # set_bio()
		# if link_id_list != None:
		# 	for link in link_id_list:
		# 		if link != ' ':
		# 			like(link)
		# if usernames !=None:
		# 	for username in usernames:
		# 		follow(username)
		logout()

driver = webdriver.Firefox()
# 'B-ZvdXZha17', 'B-R_W0IBEYO','B-coY20KYZV'
link_id_list = ['B-ZvdXZha17', 'B-R_W0IBEYO','B-coY20KYZV']
usernames = None
# user_id = ['paviparvathi123@hotmail.com']

with open(ASSET+'mail_id.txt', 'r') as f:
	user_id = f.readlines()

run(user_id, link_id_list, usernames)