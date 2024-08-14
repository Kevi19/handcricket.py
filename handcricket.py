# import random

# print("Welcome to HandCricket")
# # choice=(input("choose batting or bowling:"))
# print("1 : for batting")
# print("2 : for batting")
# choice=int(input("choose batting or bowling:"))

# def score():
#         global r
#         r=0
#         while True:
                
            
#                 user=int(input("user  runs:"))
#                 computer=random.randint(1,6)
#                 print("computer:",computer)
                
#                 if(user==computer):
#                     print('user is out')
#                     break
#                 elif user==1 or user==2 or user==3 or user==4 or user==5 or user == 6:
#                     r=r+user
                    
#                 else:
#                     print("'invalid runs'")
                
#         print(" user total score =",r)   
# score()

# def sco():
#         global run
#         run=0
        
#         while True:
                
            
#                 user=int(input("user  bowls:"))
#                 computer=random.randint(1,6)
#                 print("computer:",computer)
                
#                 if(user==computer):
#                     print('computer is out')
#                     break
#                 elif computer==1 or computer==2 or computer==3 or computer==4 or computer==5 or computer == 6:
#                     run=run+computer
                    
#                 else:
#                     print("'invalid runs'")
#                 break
                
#         print(" computer total score =",run)   
# sco()
# if r>run:
#     print("user wins")
# else:
#     print("computer wins")



# if(choice==1):
#     score()
# elif(choice==2):
#     sco()
# else:
#     print("Invalid input")
        
    


import random

choices = ["stone", "paper", "scissor"]

player_wins = 0
computer_wins = 0
rounds = 0

while rounds < 5:
    player_choice = input("Enter your choice (stone/paper/scissor): ")
    computer_choice = random.choice(choices)

    print(f"\nPlayer chose: {player_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if player_choice.lower() not in choices:
        print("Invalid choice. Please try again.\n")
        continue

    if player_choice.lower() == computer_choice:
        print("It's a tie!\n")
    elif (player_choice.lower() == "stone" and computer_choice == "scissor") or \
            (player_choice.lower() == "paper" and computer_choice == "stone") or \
            (player_choice.lower() == "scissor" and computer_choice == "paper"):
        print("Player wins!\n")
        player_wins += 1
    else:
        print("Computer wins!\n")
        computer_wins += 1

    rounds += 1

print("Game over!")

if player_wins > computer_wins:
    print("Player wins the game!")
elif player_wins < computer_wins:
    print("Computer wins the game!")
else:
    print("It's a tie!")




