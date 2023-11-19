# Created on Sun Nov 19 14:44:36 2023
# Author: @AngelaTeyvi
# Code to learn boolean, functions, and conditional statement (if else)
# There is a blog post about it here
# This simple code checks if the door is open or not and prints a statement

import random

door_closed_status = random.choice([True, False])

# Function to check if the door is locked
def locked_door():
    global door_closed_status
    door_closed_status = True
    # Sends internal communication that the door is locked

# Function to check if the door is unlocked
def unlocked_door():
    global door_closed_status
    door_closed_status = False
    # Sends internal communication that the door is unlocked

# Check if the door is unlocked
if door_closed_status:
    print('It\'s Open - Should I close it?')
    # Advanced code version can take an action to close the door
    locked_door()
else:
    print('It\'s closed - Should I open it?')
    # Advanced version will include actions by the program to open the door
    unlocked_door()

# Print the final door status
print('Final door status:', door_closed_status)

