import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
draws = 0

while True:
    user = input("Enter rock, paper, or scissors: ").lower()
    
    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("Draw")
        draws += 1

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore Board")
    print("You:", user_score)
    print("Computer:", computer_score)
    print("Draws:", draws)

    play = input("Play again? (yes/no): ").lower()

    if play != "yes":
        break

print("\nFinal Score")
print("You:", user_score)
print("Computer:", computer_score)
print("Draws:", draws)
