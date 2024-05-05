import cmath



# I used the formula method in this function 
def solvequadeq(a, b, c):
    D = b**2 - 4 * a * c
    x1 = (-b - cmath.sqrt(D)) / (2 * a)
    x2 = (-b + cmath.sqrt(D)) / (2 * a)
    return x1, x2
while True:
	print(' This is a quadratic equation solver\nenter s to start or e to quit[s/e]')
	user_input=input()
	if user_input =='s':
		a =int(input('Enter a:'))
		b = int(input('Enter b:'))
		c = int(input('Enter c:'))

		print(f'Equation: {a}x² + {b}x + {c} = 0')
		solutions = solvequadeq(a, b, c)
		print('Roots:')
		print(f'x1 = {solutions[0].real}')
		print(f'x2 = {solutions[1]. real}')
	elif user_input =='e':
		break
else:
	print('invalidinput entered !!')

	
	
	
