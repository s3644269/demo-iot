"""
Write a Python program to count the number of strings where the string length is 2 or more
and the first and last character are same from a given list of strings.

"""


def compare_strings(strings):
    for string in strings:
        str_length = len(string)
        if str_length > 1:
            first_ch = string[0]
            last_ch = string[str_length - 1]
            if first_ch == last_ch:
                print(string)


if __name__ == '__main__':
    str = {
        'abba',
        'bba',
        'acca',
        'a'
    }
    compare_strings(str)
