# height needs to be above 120cm
# age requirements for the price of a ticket
# <12 $5
# 12 - 18 $7
# >18 $12
# if yes they get a ticket and can ride
# if not they cannot ride


print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))

if height >= 120:
    age = int(input("how old are you?"))
    if age < 12:
        print("Your ticket cost is 5 dollars")
    elif age <= 18:
        print("your ticket cost is 7 dollars")
    else:
        print("your ticket costs 12 dollars")
else:
    print("sorry you arent tall enough.")
