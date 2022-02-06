
greeting = input('Hello!  What would you like reveresed?\n')
list = greeting[::-1]
print(list)

def closing():
    closing_stmt = input("would you like to try again?\n")


def play():
    again = input("Great! What would you like reversed?\n")
    list_2 = again[::-1]
    print(list_2)
    closing()



if closing == 'yes':
    play()    
else:
    print("Thanks for playing!")

    


