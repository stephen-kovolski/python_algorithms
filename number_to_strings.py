#We need a function that can transform a number into a string.


greeting = input("What would you like converted, a string or an integer?\n")

if greeting == "integer":
    converted_int_greeting = input("What int would you like converted to a string?\n")
    converted_int_greeting = str(converted_int_greeting)
    print(type(converted_int_greeting))
    print(converted_int_greeting)

elif greeting == "string":
    converted_str_greeting = input("What string would you like converted to a int?\n")
    converted_str_greeting = int(converted_str_greeting)
    print(type(converted_str_greeting))
    print(converted_str_greeting)

else:
    print("Please choose integer or string as a choice")
