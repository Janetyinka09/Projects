#my project (a code to build a rock, paper and scissors game)
import random 
Intro = "You have successfully entered into a game of rock, paper and scissors and you'll be playing against a computer...Good luck!!!"
print(Intro)
choices = ["rock", "paper", "scissors"] 
user = input("Enter your choice; rock, paper, scissors :").replace(" " , "")
computer = random.choice(choices)
if user == computer : 
    print(f"It's a tie...Computer picked {computer}") 
elif (user == "rock" and computer == "scissors") or \
(user == "scissors" and computer == "paper") or \
(user == "paper" and computer == "rock") : 
    print(f"Computer chooses {computer} so apparently, you won") 
else:
    print(f"You lost, computer chose {computer}... try again loser!!! ") 
    