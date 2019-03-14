"""
Write a Python class to reverse a string word by word.
Input string : 'hello .py'
Expected Output : '.py hello'
"""


def reverse_strings():
    input_string = input("Enter a sentence: ")
    str_array = []
    temp_str = ''
    for i in range(0, len(input_string), 1):
        if input_string[i] != ' ':
            temp_str += input_string[i]
        else:
            str_array.append(temp_str)
            temp_str = ''
    str_array.append(temp_str)

    for str in str_array:
        print(str)


if __name__ == '__main__':
    reverse_strings()
