import instaloader
from asset.personal import password, username, my_circele_users

ASSET = 'asset/'
L = instaloader.Instaloader()
# Login or load session
L.login(username, password)        # (login)
# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "queen_paviparvathi")
# Print list of followees
with open(ASSET+"followers.txt", 'w') as file:
	for followee in profile.get_followers():
	    username = followee.username
	    if username not in my_circele_users:
		    file.write(username + "\n")
		    print(username)

