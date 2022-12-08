# Hangman on Python

This game is a basic hangman made automated using Python.
The coding style is highly modular, with one main executable code "Hangman.py",
and 6 other modules to support the gameplay.

## LIST OF MODULES:
1. "WordBank.py": main function is to extract random words from twitter for the game play
2. "WordSelector.py": from the word bank, random choose a word for the game play
3. "HangTheMan.py": generates the graphics of the hangman
4. "CharacterMatch.py": compares imput letter with the letters of the secret word to determine if the guess is right
5. "GameTracker.py": tracks the progress of the game and determine if the round is over
6. "ListGenerator.py": creates guessWord list

## ver 0.1:
Gameplay experience meets expectations; time taken to create word bank is longer than expected.

Possible improvements:
- Create an offline extension where word bank is readily available and without twitter scraping
- Increase the number of chance from 8 to 10
- Different difficulty levels
- Provides definition of the word at the end of the round 
- More efficient way to create graphics in "HangTheMan.py"

Best practice: no more than 50 lines per module
- "Hangman.py": 66 lines
- "WordBank.py": 31 lines
- "WordSelector.py": 9 lines
- "HangTheMan.py": 49 lines
- "CharacterMatch.py": 15 lines
- "GameTracker.py": 9 lines
- "ListGenerator.py": 10 lines
Total no. of lines: 189
