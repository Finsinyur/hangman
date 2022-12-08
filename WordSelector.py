# word selector
# Import module
import random

def wordSelector(x): # x is a list
	wordSelected = random.choice(x) #a random word is chosen
	gameCharacters = list(wordSelected) #the random word has been split into its constituent letters
	
	return wordSelected, gameCharacters # returns the word and its letters in the form of tuples (str, list)