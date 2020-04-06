from instapy_cli import client
from textwrap import dedent

username = 'queen_paviparvathi'
password = 'qwerty123456'
image = 'post.jpg'
text = dedent('''
	hi''')

with client(username, password) as cli:
	cli.upload(image, text)

