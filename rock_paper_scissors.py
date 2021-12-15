import random
import sys


greeting = input("would you like to play rock, paper, scissors? \n")
if greeting != "yes":
    sys.exit("oh well, have a nice day")
else :
    player_choice = input("whats your choice? \n")


list = ["rock", "paper", "scissors"]
computer_choice = random.choice(list)

if player_choice == computer_choice:
    print("its a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("you win! The computer picked \n" + computer_choice)
elif player_choice == "scissors" and computer_choice == "paper":
    print("you win! The computer picked \n" + computer_choice)
elif player_choice == "paper" and computer_choice == "rock":
    print("you win! The computer picked \n" + computer_choice)
else:
    print("sorry, you lost. The computer picked\n" +  computer_choice)



