from operator import itemgetter

# we can store test data in this module like users

users = [
	{"name": "DoanThao", "email": "0368775123", "password": "02071991"},
	{"name": "invalid_user", "email": "", "password": ""},
	{"name": "invalid_email", "email": "staff@test.com", "password": "qwert1235"},
	{"name": "invalid_password", "email": "0368775123", "password": "qwert1234"},
	{"name": "Admin1", "email": "admin@test.com", "password": "qwert1234"},
	{"name": "Admin2", "email": "admin@test.com", "password": "qwert1234"},
]

def get_user(name):
	try:
		return (user for user in users if user["name"] == name).__next__()
	except:
		raise
		print("\n     User %s is not defined, enter a valid user.\n" %name)