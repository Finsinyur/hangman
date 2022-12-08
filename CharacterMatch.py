# character matching
def characterMatch(x,y,z):
#x is the true word list, y is the guess word list, z is the user input
	i = 0 # universal counter
	j = 0 # win counter
	w=0
	while i < len(x):
		if z == x[i]:
			y[i] = z
			j = j+1
		i = i+1
	if j != 0:
		return y
	else:
		return w