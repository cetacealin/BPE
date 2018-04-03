#practice from: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#Print out that many copies of the previous message on separate lines.
def invalid_data(age, copy):
	if (age or copy) <=0:
		raise ValueError('This is invalid.')


def main():
	try:
		name = input('Give me your name: ')
		user_age = int(input('Give me your age: '))
		copy_num = int(input('How many copy do you want? Enter: '))
	except ValueError:
		print('This is invalid.')
	invalid_data(user_age, copy_num)
	output_year = 2018 - user_age + 100
	output = '\nYour name is {}, and you\'ll be 100 years old in {}'.format(name, output_year)
	print(copy_num * output)


if __name__ == "__main__":
	main()
