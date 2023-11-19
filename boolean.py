#Created on Sun Nov 19 14:44:36 2023
#author: @AngelaTeyvi
#code to learn boolean, functions and conditional statement (if else)
#There is a blog post about it here
#this simple code check if the door is open or not and prints a statement

import random

door_closed_status = random.choice([True,False])

# function to check if door is locked
def locked_door():
	global door_closed_status
	door_closed_status = True
#sends internal communication that the door is unlocked

# fuction to check if door is unlocked
def unlocked_door():
	global door_closed_status
	door_closed_status = False
#sends an internal communication that the door is locked



# check if door is unlocked
if door_closed_status:
	print('Its Open- Should I close it?')
	locked_door()
#advance code version can take an action to close the door

else:
	print('its closed- should I open it?')
	unlocked_door()
#advanced version will include actions by the program to close the door

