# Import all important modules

import WordBank as wB # Word bank from twitter
import WordSelector as wS # Engine to select a random word from a list of words
import HangTheMan as hTM # Hangman Illustrations
import CharacterMatch as cM # check and match input with the characters of the word
import GameTracker as gT # track if the game has been won
import ListGenerator as lG # generate empty list with the correct no. of elements
import CharChecker as cC # check if character has been tried before

# Global Variables
totalChance = 8
winCount = 0
loseCount = 0



print ("This is a beta of the Hangman Game by Caden Lee.") # Introduction
print ("Please follow the instructions strictly.")
print("Please wait while we prepare the game...")
secretList = wB.WordBank() # A list of secret words is chosen
Play = input("Do you wish to play this game? (Y/N): ").upper()

# Begins play loop
while Play == "Y":
	chanceLeft = 8 
	wrongCount = 0
	charRecord = []
	secretWord, secretChar = wS.wordSelector(secretList) # A secret word is chosen
	guessWord = lG.listGen(secretChar)
	while chanceLeft > 0:
		# Request player input
		guessChar = input("Please guess a letter (a to z, including hyphen '-'): ")
		if guessChar == "%":
			chanceLeft = 0
			break
		roundStatus = cM.characterMatch(secretChar, guessWord, guessChar )
		if roundStatus == 0:
			wrongCount = wrongCount + 1
			chanceLeft = totalChance - wrongCount
			print("Wrong Guess! Try again! you have "+str(chanceLeft)+" chance(s) left!")
			hTM.HangMan(wrongCount)
			print (guessWord)
		else:
			print("Right Guess! Keep going, good luck!")
			guessWord = roundStatus
			print(guessWord)
		if gT.gameTracker(secretChar, guessWord) == 1:
			print("Hooray! You win!")
			print(guessWord)
			hTM.HangMan(wrongCount)
			winCount = winCount+1
			chanceLeft = 0
			Play = input("Do you wish to play again? (Y/N): ").upper()
		else:
			if chanceLeft == 0:
				print("Boohoo! You lose!")
				print("The correct answer is: "+secretWord)
				print("Your answer is: "+str(guessWord))
				print("Try again next time!")	
				loseCount = loseCount + 1
				Play = input("Do you wish to play again? (Y/N): ").upper()
			else:
				continue
print("+++++++++++++++END GAME+++++++++++++++++++")
print("Total number of wins: "+str(winCount))
print("Total number of loses: "+str(loseCount))
print("Thanks for playing! See you again!")