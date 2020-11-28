from gameComponents import gameVars

# define a win or lose function
def winorlose(status):
	# print("inside winorlose functions: status is: ", status)

	print("You" , status, "! Would you like to play again?")
	choice = input ("Y / N? ")

	if choice == "Y" or choice == "y":
		# reset the game and start over again

		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False

	elif choice == "N" or choice == "n":
		# exit message and quit
		print("You chose to quit. Thanks for playing.")
		exit()
	else:
		print("Make a valid choice - Y or N")
		#this wil generate a bug that we need to fix later
		choice = input("Y / N: ")