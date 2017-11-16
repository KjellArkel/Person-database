################ ToDo's #################
# @ToDo Add comments to the code in functions.py
# @ToDo Add clear statments in code (functions)
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
	# Prints out the commands that the user can use
	print("Enter 'DONE' if you are finished")
	print("Enter 'HELP' for help")
	print("Enter 'NDB' for a new database")
	print("Enter 'NEW' for adding a new person")

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
		ybirth int(2)
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
	# ask the user his/her first name
	firstname = input("What is the firstname? ").capitalize()
	
	check_mid_name = True
	while check_mid_name:
		have_middlename = input("Does this person have a middle name? ").lower()
		if have_middlename == 'yes' or have_middlename == 'y' or have_middlename == 'ja' or have_middlename == 'j':
			midname = input("What is the person middle name? ").lower()
			check_mid_name = False
		elif have_middlename == 'no' or have_middlename == 'n' or have_middlename == 'nee':
			check_mid_name = False
		else:
			print('That is not a legit anwser. Try it again.')

	lastname = input("What is the lastname? ").capitalize()
	
	clear_screen()

	loop_phonenumber = True

	while loop_phonenumber:
		phonenumber = input("What is the phonenumber? ")
		check_phonenumber = phonenumber.isdigit()
		if check_phonenumber is False:
			print('That is not legit. Try it again.')
		else:
			loop_phonenumber = False

	print("If you are a male type 'm'")
	print("If you are a female type 'f'")

	while True:
		gender = input("What is your gender? ")
		if gender == 'gn':
			print('LOL')
			break
		elif len(gender) >= 2:
			print('You didnt read the discription. Will go faster if you do!')
		else:
			break

	print('For the next three questions use numbers.')
	while True:
		birthday = input('What is your day of birth? ')
		check_birthday = birthday.isdigit()
		if check_birthday is False:
			clear_screen()
			print('That is not a number!')
		elif len(birthday) >= 3:
			clear_screen()
			print("Your use more than 2 numbers.")
			print("Please use 2 numbers.")
		elif len(birthday) <= 1:
			clear_screen()
			print("You used less than 2 numbers.")
			print("Please use 2 numbers.")
		elif int(birthday) >= 31 or int(birthday) <= 0:
			clear_screen()
			print("Every month has 30 or 31 days not " + birthday + " days")
		else:
			break

	while True:
		month_of_birth = input('What is the month you were born in? ')
		check_month_of_birth = month_of_birth.isdigit()
		if check_month_of_birth is False:
			clear_screen()
			print('That is not a number!')
		elif len(month_of_birth) >= 3:
			clear_screen()
			print("Your use more than 2 numbers.")
			print("Please use 2 numbers.")
		elif len(month_of_birth) <= 1:
			clear_screen()
			print("You used less than 2 numbers.")
			print("Please use 2 numbers.")
		elif int(month_of_birth) >= 31 or int(month_of_birth) <= 0:
			clear_screen()
			print("Every year has 12 months not " + month_of_birth + " months")
		else:
			break

	while True:
		year_of_birth = input('What is the year you were born in? (4 numbers)')
		check_year_of_birth = year_of_birth.isdigit()
		now = datetime.datetime.now()
		if check_year_of_birth is False:
			clear_screen()
			print('That is not a number')
		elif len(year_of_birth) >= 5:
			clear_screen()
			print('You used more than 4 numbers.')
			print('Please use 4 numbers')
		elif len(year_of_birth) <= 3:
			clear_screen()
			print('You used less than 4 numbers.')
			print('Please use 4 nubmers')
		elif int(year_of_birth) > now.year:
			print('We are not in that year jet')
		else:
			break
