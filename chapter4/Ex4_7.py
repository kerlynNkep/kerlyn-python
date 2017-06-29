#game of chance

import random

def guess():
	num1 = random.randrange(1,1001)
	print "I have a number between  1 and 1000. Can you guess my number?"
	print "Pls type your first guess"
	num1 = int(num1)
	return num1


number = guess()
	
num2 = int(raw_input())


while 1:
	if (number==num2):
		print "Excellent! You guessed the number!"
		i = raw_input("would u like to play again (y or n)")
		i = str(i)

		if(i=="y"):
			number = guess()
			num2 = raw_input()
		else:
			print "Goodbye"
			break

	else:
		if (number>num2):
			print "your guess is too low"
			num2 = int(raw_input("Try again"))
		else:
			print "your guess is too high"
			num2 = int(raw_input("Try again"))
			








