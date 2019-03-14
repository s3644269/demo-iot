"""
Write a Python program to construct the following pattern, using a nested for loop.
*           line=1,
* *         line=2,
* * *
* * * *
* * * * *
* * * *     line=6, stars=4
* * *
* *
*
"""


def print_stars():
    lines = input('Enter the number of lines: ')
    lines = int(lines) + 1
    if lines % 2 != 0:
        print('Lines are not odd')
        return

    mid_value = int(lines / 2)
    for i in range(1, lines, 1):
        for j in range(0, mid_value - abs(i - mid_value), 1):
            print("*", end="")
        print()


if __name__ == '__main__':
    print_stars()
