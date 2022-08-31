from time import sleep
from random import *
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yourNumber = int(input('Choose a number from 1-10: '))
randomNumber = random.choice(numbers)

sleep(1)

print('The number was.....' + str(randomNumber))

sleep(0.5)

if yourNumber == randomNumber:
    print('Congrats! You have guessed the number! :) ')
elif yourNumber != randomNumber:
    print('You did not guess the number! :( ')
