import random

randomize = ("rock", "paper", "scissors")

computer = random.choice(randomize)

man = input("rock || paper || scissors: ").lower()

print(f"Player 1: {man}")
print(f"Player 2: {computer}")

if man == computer:
    print("It's a tie!")
elif (man == "rock" and computer == "scissors") or \
     (man == "paper" and computer == "rock") or \
     (man == "scissors" and computer == "paper"):
    print("You win! 🎉")
elif man in randomize:
    print("Computer wins! 😢")
else:
    print("Invalid choice! Please enter rock, paper, or scissors.")
