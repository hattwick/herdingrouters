# Random number test

import random

secretNumber = random.randint(1,100)

print('What is the random number between 1 and 100?')

# Take six guesses
for guessesTaken in range(1,8):
    print('Take a guess:')
    guess = int(input())

    if guess < secretNumber:
        print ('Guess is low.')
    elif guess > secretNumber:
        print ('Guess is high.')
    else:
        break    # guess was correct

if guess == secretNumber:
    print('You guessed the number correctly. ' + str(guessesTaken) + ' guesses used.')
else:
    print ('Failed.  The correct number was ' + str(secretNumber))

# end 
