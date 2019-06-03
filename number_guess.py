#import random module
import random
#import system module to terminate later
import sys
#generate random number
random_int = random.randint(0,10)
#print introduction
print('I\'m thinking of a number between 1 and 10!')
guess_1 = int(input('What\'s your guess? '))
if guess_1 == random_int:
    print('You got it!')
    print('The secret number was ', random_int,'.', sep='')
    print('It took you 1 try to guess the number.')
    sys.exit
if guess_1 > random_int:
    print('Too high try again.')
if guess_1 < random_int:
    print('Too low try again.')
guess_2 = int(input('What\'s your guess? '))
if guess_2 == random_int:
    print ('You got it!')
    print('The secret number was ', random_int,'.', sep='')
    print('It took you 2 tries to guess the number.')
    sys.exit
if guess_2 > random_int:
    print('Too high try again.')
if guess_2 < random_int:
    print('Too low try again.')
guess_3 = int(input('What\'s your guess? '))
if guess_3 == random_int:
    print ('You got it!')
    print('The secret number was ', random_int,'.', sep='')
    print('It took you 3 tries to guess the number.')
    sys.exit
if guess_3 > random_int:
    print('Too high try again.')
if guess_3 < random_int:
    print('Too low try again.')
print('The secret number was ', random_int,'.', sep='')
print('You didn\'t guess the number.')
