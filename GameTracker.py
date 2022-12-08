# Keep track of the game
def gameTracker(x,y):
	#x is the true word list, y is the guess word list
	if x == y:
		w = 1
		return w
	if x != y:
		w = 0
		return w