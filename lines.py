# implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

import sys

data = """
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
6kjugi
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
_blah
20twenty
"""


def main():
    info = data.split('\n')
    count = 0

    for line in info:
        if line and (line[0].isalpha() or line[0] == '_'):
            count += 1

    print(f"The number of lines of code equals {count}")

if __name__ == "__main__":
    main()










# file = open(sys.arg[1])
    # for lines in file:
    #     if 