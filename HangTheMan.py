# Pictorial for hangman

def HangMan(x):
	if x == 1:
		print('_')

	elif x == 2:
		print('_')
		print(' |')

	elif x == 3:
		print('_')
		print(' |')	
		print(' O')

	elif x == 4:
		print('_')
		print(' |')	
		print(' O')
		print('|')
	
	elif x == 5:
		print('_')
		print(' |')	
		print(' O')
		print('/|')

	elif x == 6:
		print('_')
		print(' |')	
		print(' O')
		print("/|\\" )

	elif x == 7:
		print('_')
		print(' |')	
		print(' O')
		print('/|\\')
		print(' / ')

	elif x==8:
		print('_')
		print(' |')	
		print(' O')
		print('/|\\')
		print(' /\\')
	
	else:
		return