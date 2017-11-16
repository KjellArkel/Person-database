# Import the required moduls
import os
import functions

# Start the loop to process the command of user
while True:
	# Ask the user what to do
	command = input("What do you want to do? > ").lower()

	# If command is same as done do this
	if command == 'done' or command == 'd':
		break

	# If command is same as help do this
	elif command == 'help' or command == 'h':
		functions.show_help()
		continue

	# If command is same as new table do this
	elif command == 'new table' or command == 'ntb':
		functions.creat_table()
		continue

	# If command is same as new do this
	elif command == 'new' or command == 'n':
		functions.new_person()
		continue

	# If command is same as show do this
	elif command == 'show' or command == 's':
		show_persons()
		continue

	# If command is not equal to anything than do this
	else:
		print('This is not a legit command')