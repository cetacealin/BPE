'''Let's say I give you a list saved in a variable: : a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it. '''

def select_even(list):
    new_list = []
    for num in list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(select_even(a))
