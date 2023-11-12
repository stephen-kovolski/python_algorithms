"""
implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn't an accepted denomination.

accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
"""


def main():

    total_due = 50

    while total_due > 0:
        received = int(input("Insert a coin: "))
        print(type(received))
        if received == 25 or 10 or 5:
            total_due -= received
            print(total_due)    
        else: 
        
    

main()
    
