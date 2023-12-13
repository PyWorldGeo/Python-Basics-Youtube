from random import choice

choices = ["rock", "scissors", "paper"]

computer_score = 0
human_score = 0

while human_score < 3 and computer_score < 3:
    human_choice = input(f"Enter your choice ({choices[0]}, {choices[1]}, {choices[2]}): ").lower()
    if human_choice in choices:
        computer_choice = choice(choices)
        print(computer_choice)

        draw = human_choice == computer_choice

        human_scores1 = human_choice == "rock" and computer_choice == "scissors"
        human_scores2 = human_choice == "scissors" and computer_choice == "paper"
        human_scores3 = human_choice == "paper" and computer_choice == "rock"


        if draw:
            print("Draw!")

        elif human_scores1 or human_scores2 or human_scores3:
            print("Human wins!")
            human_score += 1

        else:
            print("Computer wins!")
            computer_score += 1
    else:
        print("Enter correct choice!")


print(f"Computer: {computer_score} / Human: {human_score}")