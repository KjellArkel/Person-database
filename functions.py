import mysql.connector

def show_help():
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

	# Ask the user what the name of the table
	name_new_table = input("What is the name of the new table? > ").lower()

	# Create a new table 
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
		# Execute the SQL command
		cursor.execute(sql)
		# Commit your changes in the database
		db.commit()
	except:
		# Rollback in case there is any error
		db.rollback()
		print('aborted')

	# disconnect from server
	db.close()

def new_person():
	# login to the server
	db = login()
	cursor = db.cursor()

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
	print("If you don't know than type 'ng'")
	gender = input("What is your gender? ")

	while True:
		if len(gender) == 1 or gender == 'ng':
			if gender == 'ng':
				print('LOL')
		else:
			print('You didnt read the discription. Will go faster if you do!')


