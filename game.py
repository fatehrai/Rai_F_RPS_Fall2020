# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose, comparisons

# set up our game loop
while gameVars.player is False:
	# this is the player choice
	print("===========*/ RPS! /===========")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("======================")
	print("Choose your weapon! or type quit to exit\n")
	
	gameVars.player = input ("Choose rock, paper or scissors: \n")

	# if the player chooses to quit, then don't do anything else
	# just exit the process (Kill Python) and quit the game
	if gameVars.player == "quit":
		print("You chose to quit, quitter!")
		exit()

	# this will be the Computer choice -> a random pick from the choices array
	computer = gameVars.choices[randint(0,2)]

	# check to see what the user input 

	# just validate that i can make a choice

	# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
	print("You chose: " + gameVars.player)

	# validate that the random choice worked for the Computer
	print("Computer chose: " + computer)

	comparisons.comparisonfn(gameVars.player)

	# check gameVars.player lives and computer lives
	if gameVars.player_lives == 0:
		winLose.winorlose("lost")

	elif gameVars.computer_lives == 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False

	print("player lives:", gameVars.player_lives, "lives left")
	print("computer lives:", gameVars.computer_lives, "lives left")
	

