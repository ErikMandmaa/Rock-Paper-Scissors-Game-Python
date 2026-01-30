import random

player = int(input("Pick a number from 1 to 3: "))

computer = random.randint(1, 3)

choices = {1: "rock", 2: "paper", 3: "scissors"}
print()

print(f"You chose: {choices[player]}")
print(f"The computer chose: {choices[computer]}")

if player == computer:
    print("It's a tie!")

if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
    print("You win!")
elif (computer == 1 and player == 3) or (computer == 2 and player == 1) or (computer == 3 and player == 2):
    print("The computer wins!")
