# import the required moduls
import os
import functions

# start the loop to process the command of user
while True:
	# ask the user what to do
	command = input("What do you want to do? > ").lower()

	# exit the program
	if command == 'done' or command == 'd':
		break

	# print out the help function
	elif command == 'help' or command == 'h':
		functions.show_help()
		continue

	# creates a new table in the database
	elif command == 'new table' or command == 'ntb':
		functions.creat_table()
		continue

	# create a new person
	elif command == 'new' or command == 'n':
		functions.new_person()
		continue

	# Is the command is not legit print this
	else:
		print('This is not a legit command')