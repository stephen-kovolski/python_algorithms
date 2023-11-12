"""
loop through the string
find the uppercase letter
split where the uppercase letter is
join the string with _
"""
    

        

def add_underscore_to_uppercase():

    string = input("Enter a string: ")

    modified_string = ""
    
    for char in string:
        if char.isupper():
            modified_string += "_" + char
        else:
            modified_string += char
    
    x = modified_string.lower()
    print(x)

add_underscore_to_uppercase()