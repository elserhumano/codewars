# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# Example:
#         create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!


def get_n_chars(str_num, start, end):
    temp = ''
    for i in range(start, end+1):
        temp += str(str_num[i])
    return temp


def create_phone_number(n):
    return '(' + get_n_chars(n, 0, 2) + ') ' + get_n_chars(n, 3, 5) + '-' + get_n_chars(n, 6, 9)


def create_phone_number2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)




print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # => returns "(123) 456-7890"

print(create_phone_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # => returns "(123) 456-7890"