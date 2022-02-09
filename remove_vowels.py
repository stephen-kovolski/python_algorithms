
import re
from tkinter import E

comment_one = ["this is the comment"]
vowels = {
    'A': 'a',
    'E': 'e',
    'I': 'i',
    'O': 'o',
    'U': 'u'
}
new_comment = ""

for vowels in comment_one:
    comment_one.remove(vowels)
    print(comment_one)
    print(vowels)

