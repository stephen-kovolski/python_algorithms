#ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

#If the function is passed a valid PIN string, return true, else return false.

#Need to verify that there are only int's in the pin and reject it if there is anything else entered.



pin = input("Please enter your pin to continue\n")

if len(pin) == 4:
    converted_pin = int(pin)
    print(type(pin))
    print("You've entered a four digit pin")
elif len(pin) == 6:
    print("You've entered a 6 digit pin")
else:
    print("incorrect pin")
