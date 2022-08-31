

import re 

def strong_password(users_password):
	if len(users_password) >= 8:
		user_password_list=users_password.split()
		lower_letters=[chr(i) for i in range(97,123)]
		upper_letters=[chr(i) for i in range(65,91)]
		numbers=[i for i in range(10)]
		if  not any(item in users_password for item in lower_letters):
			return 'password must contain a lower letter'
		if not any(item in users_password for item in upper_letters):
			return 'password must contain an uppercase letter'
		if not any(str(item) in users_password for item in numbers):
			return 'number is required'
		else:
			return 'password is strong'
	else:
		return 'password must be 8 character long'

def strong_password_regex(users_password):
    
	upper_regex = re.compile(r'[A-Z]+') #upper letters
	lower_regex = re.compile(r'[a-z]+') #lower letters
	number =re.compile(r'[0-9]+') #number 
	if not upper_regex.findall(users_password):
		return 'uppercase letter is required'
	if not lower_regex.findall(users_password):
		return 'lowercase letter is required'
	if not number.findall(users_password):
		return 'number is required'
	else:
		return 'Password is strong '
