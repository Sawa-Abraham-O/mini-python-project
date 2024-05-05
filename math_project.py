import cmath
import time

def solvesimeqn(x1,y1,c1,x2,y2,c2):
	x= ((c1*y2) - (y1*c2))/((x1*y2)-(y1*x2))
	y= ((x1*c2)-(x2*c1))/((x1*y2)-(y1*x2))
	return x, y


def solvequadeqn(a, b, c):
    D = b**2 - 4 * a * c
    x1 = (-b - cmath.sqrt(D)) / (2 * a)
    x2 = (-b + cmath.sqrt(D)) / (2 * a)
    return x1, x2


while True:
	try:
		time.sleep(2)
		print('  		welcome'.upper())
		time.sleep(1)
		print('  This is a quadratic equation solver\n  And a simultaneous equation solver program\n  Enter \'s\' to start or\'e\' to quit[s/e]: ')
		user_input=input(' ')
		if user_input =='e':
			print('     Goodbye❤️🥰💃🕺')
			print(''' 
			
	programmed  by Abraham
		💻💻💻😎😎😎😎 
			
			''')
			break
		if user_input =='s':
			time.sleep(1)
			sec_user_input =input('  What operation would you like to perform\n  Enter quad for quadratic equation or sim for simultaneous   equation [quad/sim]: ')
			if sec_user_input == 'quad': 
				a =int(input('Enter a: '))
				b = int(input('Enter b:'))
				c = int(input('Enter c:'))

				print(f'Equation: {a}x² + {b}x + {c} = 0')
				solutions_quad = solvequadeqn(a, b, c)
				print('Roots:')
				print('caclulating......')
				time.sleep(3)
				print(f'x1 ={solutions_quad[0].real}\n {round(solutions_quad[0].real,2)} rounded up to 2d.p')
				print(f'x2 ={solutions_quad[1]. real}\n {round(solutions_quad[1]. real,2)} rounded up to 2d.p')
			elif sec_user_input =='sim':
				x1= int(input('  Enter x1: '))
				y1= int(input('  Enter y1: '))
				c1= int(input(' Enter c1: '))
				x2= int(input(' Enter x2: '))
				y2= int(input('Enter y2: '))
				c2= int(input('Enter c2: '))
				print(f' {x1}x +{y1}y = {c1}')
				print(f' {x2}x +{y2}y = {c2}')
				solutions_sim = solvesimeqn(x1,y1,c1,x2,y2,c2)
				print('Roots:')
				print('caclulating......')
				time.sleep(3)
				print(f' x = {solutions_sim[0]}\n {round(solutions_sim[0],2)} rounded up to 2d.p')
				print(f' y ={solutions_sim[1]}\n {round(solutions_sim[1],2)} rounded up to 2d.p')
			elif sec_user_input != 'sim' or 'quad':
				print('Enter valid input !!!😡😡😡'.upper())
		elif user_input != 's' or 'e':
			print(" ENTER 's' OR'e'!!!😡😡😡")	
		
	except ZeroDivisionError as e:
		print(f'Error: {e}')
		continue
	except ValueError:
		print('enter valid number !!!😡😡😡😡'.upper())	 
		continue
		
	

	
		
	

	
	
	
