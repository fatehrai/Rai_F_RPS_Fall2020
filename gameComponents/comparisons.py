from random import randint

from gameComponents import gameVars

computer = gameVars.choices[randint(0,2)]

def comparisonfn(status):
	
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
			