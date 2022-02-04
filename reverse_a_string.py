
greeting = input('Hello!  What would you like reveresed?\n')
list = greeting[::-1]
print(list)

closing = input("would you like to try again?\n")

if closing == 'yes':
    again = input("Great! What would you like reversed?\n")
    list_2 = again[::-1]
    print(list_2)
    closing
    
else:
    print("Thanks for playing!")

    