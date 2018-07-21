'''Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)'''

def palindrome(user_str):
    return user_str == user_str [::-1]

get_word = input("Enter a word: ")
print(palindrome(get_word))


