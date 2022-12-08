# Guess word list generator

def listGen(x): # x is the list of the secret word
	i = len(x)
	j = 0
	y = []
	while j < i:
		y.append(" ")
		j = j+1
	return y