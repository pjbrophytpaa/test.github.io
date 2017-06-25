# The Monty Hall Problem
# Similar to the game from "Let's Make a Deal"
# There are 3 doors. 1 is a winner. 2 are jokes.
# Contestant picks a door. A fake door is revealed.
# Contestant has option to switch to the remaining door.
# Door choice is revealed.

import numpy as np
import cv2
import random
import time

print('+ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('+  __                  __   __                 __       __            __                   +')
print('+ |  \                |  \ |  \               |  \     /  \          |  \                  +')
print('+ | $$       ______  _| $$_| $$ _______       | $$\   /  $$  ______  | $$   __   ______    +')
print('+ | $$      /      \|   $$ \\$ /       \       | $$$\ /  $$$ |      \ | $$  /  \ /      \   +')
print('+ | $$     |  $$$$$$\\$$$$$$  |  $$$$$$$       | $$$$\  $$$$  \$$$$$$\| $$_/  $$|  $$$$$$\  +')
print('+ | $$     | $$    $$ | $$ __  \$$    \       | $$\$$ $$ $$ /      $$| $$   $$ | $$    $$  +')
print('+ | $$_____| $$$$$$$$ | $$|  \ _\$$$$$$\      | $$ \$$$| $$|  $$$$$$$| $$$$$$\ | $$$$$$$$  +')
print('+ | $$      \\$$     \  \$$  $$|       $$      | $$  \$ | $$ \$$    $$| $$  \$$\ \$$     \  +')
print('+  \$$$$$$$$ \$$$$$$$   \$$$$  \$$$$$$$        \$$      \$$  \$$$$$$$ \$$   \$$  \$$$$$$$  +')
print('+                              _______                       __                            +')
print('+                             |       \                     |  \                           +')
print('+               ______        | $$$$$$$\  ______    ______  | $$                           +')
print('+              |      \       | $$  | $$ /      \  |      \ | $$                           +')
print('+               \$$$$$$\      | $$  | $$|  $$$$$$\  \$$$$$$\| $$                           +')
print('+              /      $$      | $$  | $$| $$    $$ /      $$| $$                           +')
print('+             |  $$$$$$$      | $$__/ $$| $$$$$$$$|  $$$$$$$| $$                           +')
print('+              \$$    $$      | $$    $$ \$$     \ \$$    $$| $$                           +')
print('+               \$$$$$$$       \$$$$$$$   \$$$$$$$  \$$$$$$$ \$$                           +')
print('+                                                                                          +')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('')
print('Welcome to Let\'s Make a Deal. There are 3 doors in front of you. One is a grand prize. The')
print('others are things we\'re done with. You get to pick one. Which will it be (type 1, 2, or 3)?')
door_choice = raw_input()
while door_choice != '1' and door_choice != '2' and door_choice != '3':
    print('That is not an option, try again (1, 2 or 3)')
    door_choice = raw_input()

#Decide which door is the winner, and the two losers.
door_winner = random.randint(1,3)
door_chicken = random.randint(1,3)
while door_chicken == door_winner:
    print('debug winner is',door_winner,'chicken is',door_chicken)
    door_chicken = random.randint(1,3)

door_laundry = random.randint(1,3)
while door_laundry == door_winner or door_laundry == door_chicken:
    door_laundry = random.randint(1,3)

#Decide which loser door to open
loser_1 = random.randint(1,3)
while loser_1 == door_winner or loser_1 == int(door_choice):
    loser_1 = random.randint(1,3)

print('Your choice is door number {}. Let\'s see what was behind door number {}...'.format(door_choice,loser_1))
time.sleep(3)

if door_chicken == loser_1:
    image = cv2.imread("chicken.png")
    cv2.imshow('Chicken! What will they mix it with for dinner?',image)
else: #it's laundry
    image = cv2.imread("laundry.png")
    cv2.imshow('Adrian has an announcement about this.',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

other_door = random.randint(1,3)
while other_door == loser_1 or other_door == int(door_choice):
    other_door = random.randint(1,3)
print("Nice job avoid that door! Before we open, would you like to switch your choice to door number {}? (y or n)".format(other_door))
switch_door = raw_input()
if switch_door == 'y':
    print('Okay. Your choice is changing from door number {} to door number {}.'.format(door_choice,other_door))
    door_choice = other_door
else:
    print('Okay. You are staying with door number {}'.format(door_choice))
time.sleep(2)
print("Let's see what you picked! Countdown please...")
time.sleep(3)
print("Three...")
time.sleep(1)
print("Two...")
time.sleep(1)
print("ONE!!!!...")
time.sleep(1)

if int(door_choice)== door_winner:
    image = cv2.imread("winner.png")
    cv2.imshow('Your nightmare is over.',image)
elif int(door_choice) == door_chicken:
    image = cv2.imread("chicken.png")
    cv2.imshow('Chicken! What will they mix it with for dinner?',image)
else: #it's laundry
    image = cv2.imread("laundry.png")
    cv2.imshow('Adrian has an announcement about this.',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Thanks for playing!")
