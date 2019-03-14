"""
Write a Python function that checks whether a passed string is palindrome or not.

Note: A palindrome is a word, phrase, or sequence that reads the same backward as
forward, e.g., madam, a nut for a jar of tuna
"""


def check_palindrome():
    input_string = input("Enter the string: ")
    length_string = len(input_string)
    reverse_string = ''

    temp_string = ''
    for i in range(0, length_string, 1):
        if input_string[i] != ' ':
            temp_string += input_string[i]

    input_string = temp_string
    length_string = len(input_string)

    for i in range(length_string - 1, -1, -1):
        reverse_string += input_string[i]

    check = ''
    if input_string != reverse_string:
        check = 'not '

    print(f'The input string: {input_string} is {check}the same as reverse: {reverse_string}')


if __name__ == '__main__':
    check_palindrome()
