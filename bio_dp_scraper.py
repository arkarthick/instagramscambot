import json
import requests
from bs4 import BeautifulSoup
import time
from urllib.request import urlretrieve as uret

ASSET = 'asset/'
SAVED = 'saved/'

def get_user_info(user_name):
    url = "https://www.instagram.com/" + user_name + "/?__a=1"
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Seems like dns lookup failed..')
        time.sleep(2)
        return None
    if r.status_code != 200:
        print('User: ' + user_name + ' status code: ' + str(r.status_code))
        print(r)
        return None

    info = json.loads(r.text)
  
    pic = info['graphql']['user']["profile_pic_url_hd"]
    if pic != None:
	    filename = SAVED+'images/'+user_name+'.jpg'
	    uret(pic,filename)
    bio = info['graphql']['user']["biography"]
    if bio != None and bio != ' ':
    	bio = bio.encode('ascii', 'ignore').decode('ascii')
    	with open(SAVED+'bio.txt', 'a+') as f:
    		f.write(bio)
    		f.write('\n')
    		f.write('\n')

    # info = json.dumps(info, indent=2)
    # with open('qqq.json', 'w') as f:
    # 	f.write(info)
    # print(pic)
with open(ASSET+'followers.txt', 'r')as f:
	usernames = f.readlines()

for user in usernames:
	get_user_info(user[:-1])