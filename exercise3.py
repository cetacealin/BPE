'''Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list 
that are less than 5. 
Extras:

Print a new list that has all the elements less than 5 from this list in it 
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.'''

def filter(list, user_input):
    new_list = []
    for num in list:
        if num < user_input:
            new_list.append(num)
    return new_list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_num = int(input('Enter a number: '))
print(filter(a, user_num))
