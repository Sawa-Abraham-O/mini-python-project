while True:
	print(' simple interest calculator')
	def interest(p,r,t) :
		interest= p*(r/100)*t
		return interest
	
	
	

	try:
		question1=input('welcome, enter Y to continue or N to quit [Y\\N]: ').upper()
		if question1 == 'N':
			break
		elif question1== 'Y':
			pass

		#p= int(input('input p: '))
		#r=int(input('input r: '))
		#t=int(input('input t: ')) 

		#solution=interest(p,r,t)
		
		#print(f'The interest on {p} for {t}years at {r}\%\per annum is {solution}')	