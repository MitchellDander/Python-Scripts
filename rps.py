"""Rock-Paper-Scissors game!"""
from random import randint
from time import sleep
options = ["R", "P", "S"]
LOSS_MESSAGE = "You lose!"
WINNING_MESSAGE = "You win!"
def decide_winner(user_choice, computer_choice):
	print "You chose: %s" % (user_choice)
	print "Computer selecting..."
	sleep(1)
	print "I chose: %s" % (computer_choice)
	user_choice_index = options.index(user_choice)
	computer_choice_index = options.index(computer_choice)
	if user_choice_index == computer_choice_index:
		print "It's a tie, we both chose %s" % (user_choice)
	elif user_choice_index == 0 and computer_choice_index == 2:
		print WINNING_MESSAGE
	elif user_choice_index == 1 and computer_choice_index == 0:
		print WINNING_MESSAGE
	elif user_choice_index == 2 and computer_choice_index == 1:
		print WINNING_MESSAGE
	elif user_choice_index > 2:
		print "This is an invalid option!"
		return
	else:
		print LOSS_MESSAGE
def play_RPS():
	print "Rock, Paper, Scissors Simulator!"
	user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors:")
	sleep(1)
	user_choice = user_choice.upper()
	computer_choice = options[randint(0, len(options)-1)]
	decide_winner(user_choice, computer_choice)
play_RPS()
    