#Given two integers a and b, which can be positive or negative, find the sum of all the integers 


arg1 = input("what number would you like to start with?\n")
arg2 = input("what is the second number you would like?\n")

#print("The sum of the two numbers you requested is", int(arg1) + int(arg2))

def add_number(arg1, arg2):
    sum = int(arg1) + int(arg2)

    print("The sum of the two numbers you requested is", sum)

add_number(arg1, arg2)


