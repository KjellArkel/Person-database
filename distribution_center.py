# Import the required moduls
import mysql.connector
import os

# Ask the user what to do
command_word = input("What do you want to do? > ").lower()

# Start the loop to process the command of user
while True:
	if command_word == 'done' or command_word == 'd':
		break
	elif command_word == 'help' or command_word == 'h':
		show_help()
		continue
	elif command_word == 'new' or command_word == 'n':
		add_person()
		continue
	elif command_word == 'show' or command_word == 's':
		show_persons()
		continue
	else:
		print('This is not a legit command')