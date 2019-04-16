from operator import itemgetter

# we can store test data in this module like users

users = [
	{"name": "DoanThao", "email": "0368775123", "password": "02071991"},
	{"name": "empty_value", "email": "", "password": ""},
	{"name": "invalid_email", "email": "staff@test.com", "password": "02071991"},
	{"name": "invalid_password", "email": "0368775123", "password": "qwert1234"},
	{"name": "empty_email_right_password", "email": "", "password": "02071991"},
	{"name": "right_email_empty_password", "email": "0368775123", "password": ""},
]

def get_user(name):
	try:
		return (user for user in users if user["name"] == name).__next__()
	except:
		raise
		print("\n     User %s is not defined, enter a valid user.\n" %name)