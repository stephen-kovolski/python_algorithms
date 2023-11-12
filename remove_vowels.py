
import re

comment_one = ["this is the comment"]
vowels = {
    'A': 'a',
    'E': 'e',
    'I': 'i',
    'O': 'o',
    'U': 'u'
}

for letters in comment_one:
    for key in vowels:
        new_comment = ""
        print(letters)
        print(key)
        new_comment = letters.remove(key)
        print(new_comment)


