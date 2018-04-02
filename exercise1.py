#practice from: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#Print out that many copies of the previous message on separate lines.
def main():
    name = input('Give me your name: ')
    age = int(input('Enter your age: '))
    copy = int(input('How many copy do you want? Enter here: '))
    the_year = 2018 - age + 100
    output = '\nYour name is %s, and you\'ll be 100 years old in %d '%(name, the_year)
    if copy == 1:
        return output
    return copy * output

print(main())
