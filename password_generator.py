# Password generator

import string 
import random 


word_char = string.ascii_letters+" "+string.punctuation + string.digits

word_list=[c for c in word_char]

def generate_password(n):
	'''creates password from a given range n'''
	
	
	char_choices = [random.choice(word_list) for _ in range(n)]
	
	password = "".join(char_choices)
	
	return password 
	



if __name__ == '__main__':
	
	print('''\033[96m************************************************************
*                                                          *
*          Welcome to the Password Generator Tool!         *
*                                                          *
*          Developed by Abraham Olanrewaju (SAO)           *
*                                                          *
************************************************************

This tool helps you create secure and unique passwords 
with ease. Protect your online accounts and enhance your 
digital security in just a few simple steps.

Let’s generate your perfect password!\033[00m''')
	
	
	print("\033[92m*********************************************************\033[00m")
	
	while True:
		
		try:
		
			n = int(input('\033[92mEnter length of password: \033[00m'))
			if n<=5:
				raise ValueError('Password length must be least 6 characters long.')
					
		
			print("\033[92m*********************************************************\033[00m")
			password=generate_password(n)
			
		
			print('\033[92myour newly generated password is: \033[00m'+f'\033[93m {password} \033[00m')
			
			break 
			
		except ValueError:
			print("\033[91mPlease enter valid integer for password length \033[00m")
	
	print("\033[92m*********************************************************\033[00m")

print("Thank you for using the Password Generator Tool!")