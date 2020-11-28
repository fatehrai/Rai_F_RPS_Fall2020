# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose

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

	if (computer == gameVars.player):
		print("tie")
	# always check for negative conditions first (the losing case)
	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives -= 1
			print("you lose! gameVars.player lives: ", gameVars.player_lives)
		else:
			print("you win!")
			gameVars.computer_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			gameVars.player_lives -= 1
			print("you lose! gameVars.player lives: ", gameVars.player_lives)
		else:
			print("you win!")
			gameVars.computer_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			gameVars.player_lives -= 1
			print("you lose! gameVars.player lives: ", gameVars.player_lives)
		else:
			print("you win!")
			gameVars.computer_lives -= 1

	# check gameVars.player lives and computer lives
	if gameVars.player_lives == 0:
		winLose.winorlose("lost")

	elif gameVars.computer_lives == 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False
	

