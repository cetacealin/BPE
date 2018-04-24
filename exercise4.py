def divisors():
    new_list = []
    get_num = int(input('Enter a number: '))
    range_list = list(range(1, get_num + 1))

    for num in range_list:
        if get_num % num == 0:
            new_list.append(num)
    return new_list

print(divisors())

