#Guess thw number game
import random

print('Hello, What is your name?')
name = input()

seceretNumber = random.randint(1, 20)
print('Hey, ' + name + ', I am thinking of a number between 1 and 20. Can you guess it?')

#asking user to guess numner
for numberGuesses in range(1, 7):
	print('Make a guess.')
	guess = int(input())
	if guess < seceretNumber:
		print('You guessed too low. aim higher')
	elif guess > seceretNumber:
		print('You guessed too high. Lower your standards.')
	else:
		break # This is the correct number.

if guess == seceretNumber:
	print('Good job, ' + name + '! You guessed my number in ' + str(numberGuesses) + ', tries!')
else:
	print('Nope. The number I was thinking of was ' + str(seceretNumber) + '.')
