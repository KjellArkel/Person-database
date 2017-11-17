################ ToDo's #################
# Improve the gender questions (bug that you can use a random letter)
# Continu on national function (Prevent that ppl use random letter in the national functions)
## @ToDoCreat ToDo function

# Import the required moduls
import mysql.connector
import os
import datetime

def clear_screen():
	# if operation systeem is Windows turn on this one
	os.system('cls')

	# if operationsysteem is OS turn on this one
	# os.system('clear')

def show_help():
	# clear the screen
	clear_screen()

	# Prints out the commands that the user can use
	print("Enter 'DONE' if you are finished")
	print("Enter 'HELP' for help")
	print("Enter 'NDB' for a new database")
	print("Enter 'NEW' for adding a new person")
	print("")

def login():
	# open database connection
	db = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		db="person_database",
		port=3306
	)

	# return the var that help with login
	return db

def creat_table():
	# login to the server
	db = login()
	cursor = db.cursor()

	# clear the screen
	clear_screen()

	# ask the user what the name of the table
	name_new_table = input("What is the name of the new table? > ").lower()

	# create a new table 
	sql = """CREATE TABLE """ + name_new_table + """ ( 
		id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
		firstname VARCHAR(30) NOT NULL,
		midname VARCHAR(10),
		lastname VARCHAR(30) NOT NULL,
		phonenumber int(10),
		gender VARCHAR(1),
		bbirth int(2),
		mbirth int(2),
		ybirth int(2),
		nationality VARCHAR(10)
	);"""

	try:
		# execute the SQL command
		cursor.execute(sql)
		# commit your changes in the database
		db.commit()
	except:
		# rollback in case there is any error
		db.rollback()
		print('aborted')

	# disconnect from server
	db.close()

def new_person():
	clear_screen()

	# ask the user his/her first name
	firstname = input("What is the firstname? ").capitalize()

	clear_screen()

	# start the middle name loop
	while True:
		# ask the user if they have a middle name
		have_middlename = input("Does this person have a middle name? ").lower()
		if have_middlename == 'yes' or have_middlename == 'y' or have_middlename == 'ja' or have_middlename == 'j':
			clear_screen()
			# if they have ask them what it is
			midname = input("What is the person middle name? ").lower()
			break
		elif have_middlename == 'no' or have_middlename == 'n' or have_middlename == 'nee':
			# if not exit loop
			break
		else:
			# if not true or false repeat the question
			print('That is not a legit anwser. Try it again.')

	clear_screen()

	# ask for last name
	lastname = input("What is the lastname? ").capitalize()
	
	# clear the screen
	clear_screen()

	# start the phonenumber loop
	while True:
		# ask the user for a phone number
		phonenumber = input("What is the phonenumber? ")
		# check if the phone number is only numbers
		check_phonenumber = phonenumber.isdigit()

		if check_phonenumber is False:
			# if phone number has signs or characters
			print('That is not legit. Try it again.')
		elif len(phonenumber) >= 8:
			print('You used to much digits.')
		elif len(phonenumber) <= 6: 
			print('You didnt use enough number.')
		else:
			# if not exit loop phone number
			break

	clear_screen()

	# print he available options
	print("If you are a male type 'm'")
	print("If you are a female type 'f'")

	# start gender loop
	while True:
		# ask the user what his/ her gender is
		gender = input("What is your gender? ")
		if gender == 'gn':
			# if gender neutral print this
			print('LOL')
			break
		elif len(gender) >= 2:
			# if gender var is 2 or longer print this
			print('You didnt read the discription. Will go faster if you do!')
		else:
			# exit gender loop
			break

	clear_screen()

	# give the user the requirements for the next 3 questions
	print('For the next three questions use numbers.')
	print('Not more or less than 2')

	# start the birthday loop
	while True:
		# ask the user the birthday and check if only numbers are used
		birthday = input('What is your day of birth? ')
		check_birthday = birthday.isdigit()
		if check_birthday is False:
			# if characters or signs are used print this message
			clear_screen()
			print('That is not a number!')
		elif len(birthday) >= 3:
			clear_screen()
			# if more than 2 numbers used this message will be print
			print("Your use more than 2 numbers.")
			print("Please use 2 numbers.")
		elif len(birthday) <= 1:
			clear_screen()
			# if less than 2 numbers used this message will be print
			print("You used less than 2 numbers.")
			print("Please use 2 numbers.")
		elif int(birthday) >= 31 or int(birthday) <= 0:
			# if the number is higher than 31 or lower than 0 this message will be printed
			clear_screen()
			print("Every month has 30 or 31 days not " + birthday + " days")
		else:
			# exits the loop birthday
			break

	clear_screen()

	# start the month of birth loop
	while True:
		# ask the user what the month of birth is and check if they are numbers
		month_of_birth = input('What is the month you were born in? ')
		check_month_of_birth = month_of_birth.isdigit()
		if check_month_of_birth is False:
			# if the user didnt use all numbers
			clear_screen()
			print('That is not a number!')
		elif len(month_of_birth) >= 3:
			# if the number is more then 3 digits
			clear_screen()
			print("Your use more than 2 numbers.")
			print("Please use 2 numbers.")
		elif len(month_of_birth) <= 1:
			# if the number is less then 3 digits
			clear_screen()
			print("You used less than 2 numbers.")
			print("Please use 2 numbers.")
		elif int(month_of_birth) >= 31 or int(month_of_birth) <= 0:
			# if the user used a number that is higher than 31 or less than 0
			clear_screen()
			print("Every year has 12 months not " + month_of_birth + " months")
		else:
			# exit the loop month of birth
			break

	clear_screen()

	# start the year of birth loop
	while True:
		# ask the user what the year of birth is and if the are numbers
		year_of_birth = input('What is the year you were born in? (4 numbers)')
		check_year_of_birth = year_of_birth.isdigit()
		# get the current year
		now = datetime.datetime.now()
		if check_year_of_birth is False:
			# check if all the input is number
			clear_screen()
			print('That is not a number')
		elif len(year_of_birth) >= 5:
			# check if the lenght is higher than 4
			clear_screen()
			print('You used more than 4 numbers.')
			print('Please use 4 numbers')
		elif len(year_of_birth) <= 3:
			# check if the lenght is less than 4
			clear_screen()
			print('You used less than 4 numbers.')
			print('Please use 4 nubmers')
		elif int(year_of_birth) > now.year:
			# check if the year is not above the current year
			print('We are not in that year jet')
		else:
			# exit the loop year of birth
			break

	# start the nationality loop
	while True:
		# ask the user what his/her nationality is
		print('Please use the Language Codes (3 Letters)')
		nationality = input('What is your nationality? ').capitalize()

		if nationality == 'Dutch' or nationality == 'Nl' or nationality == 'Ned':
			# if dutch verify if true
			print('Dus jij bent een nederland? ')
			nationality_check = input('Ja of nee? ').lower()
			if nationality_check == 'j' or nationality_check == 'ja' or nationality_check == 'y' or nationality_check == 'yes':
				# if dutch break loop
				print('Lekker hoor')
				break
			elif nationality_check == 'n' or nationality_check == 'nee' or nationality_check == 'no' :
				# if not dutch reset go back to start of the loop
				print('Try it again!')

		if nationality == 'Finland' or nationality == 'Fin' or nationality == 'Fi':
			# if finnish verify if true
			print('Olet siis Suomalainen')
			nationality_check = input('Kyllä tai ei? ').lower()
			if nationality_check == 'k' or nationality_check == 'kyllä' or nationality_check == 'y' or nationality_check == 'yes':
				# if finnish break loop
				print("Kiva vaikka")
				break
			elif nationality_check == 'e' or nationality_check == 'ei' or nationality_check == 'n' or nationality_check == 'no':
				# if not Finnish reset go back to start of the loop
				print("Try it again")



				
			


