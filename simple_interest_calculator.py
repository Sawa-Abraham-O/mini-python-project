while True:
	
	try:
		print(' simple interest calculator')
		
		def interest(p,r,t) :
			interest= p*(r/100)*t
			return interest
		
		
		question1=input('welcome, enter Y to continue or N to quit [Y\\N]: ').upper()
		if question1 == 'N':
			break
		
		elif question1== 'Y':
			p=int(input('enter p: '))
			r=int(input('enter r: '))
			t=int(input('enter t: '))
			
			solution= interest(p,r,t)
			
			print(f'The simple interest on {p} for {t}years at {r}% is {round(solution,2)}')
		
		elif question1 != 'N' and 'Y':
			print('Invalid input enter N or Y !!!')
	
	except ValueError as e :
			print(f'Error: {e}')
	
			