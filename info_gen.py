from random import randint

def dob():
	year= [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 90, 91, 92, 93, 94, 95, 96, 97, 98] #23
	# mon = [1,2,3,4,5,6,7,8,9,10,11,11,01,02,03,04,05,06,07, 'Jan', 'Feb', 'mar', 'April', 'May', 'JUN', 'Jul', 'augest', 'sep', 'Nov', 'Dec']#30
	date = [1,2,3,4,5,6,7,8,9,10,11,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]#28
	sep_l= ['.', '/', '-']
	mon= [1,2,3,4,5,6,7,8,9,10,11,12]
	sep = sep_l[randint(0,2)]
	dob_l = [str(date[randint(0,27)])+sep+ str(mon[randint(0,11)]) +sep+ str(year[randint(0,22)]),
			str(date[randint(0,27)])+sep+ str(mon[randint(0,11)]),
			str(mon[randint(0,11)])+sep+ str(date[randint(0,27)]) +sep+ str(year[randint(0,22)]),
			None]

	return dob_l[randint(0,3)]


def links():

	links_l = ['https://www.instagram.com/p/B-cmzNflhGZ/?utm_source=ig_web_copy_link',
	'https://www.instagram.com/p/B-eQIweF28V/?utm_source=ig_web_copy_link']

	other_links = []

'''

def bio(gender):
	with open('male_bio.txt', 'r') as file:
		male_bios = file.readlines()

	with open('female_bio.txt', 'r') as file:
		female_bios = file.readlines()

	# if gender =='m':
'''

