import random

while True:
    my_choice = input("rock, paper, scissors: ")
    permissable_input = ["rock", "paper", "scissors"]
    pc_choice = random.choice(permissable_input)
    print(f"\nYou chose {my_choice}, laptop chose {pc_choice}.\n")

    if my_choice == pc_choice:
        print(f"Both players selected {pc_choice}. Tie")

    elif my_choice == "rock":
        if pc_choice == "scissors":
            print("Rock smashes scissors,won")
        else:
            print("Paper covers rock,lost.")

    elif my_choice == "paper":
        if pc_choice == "rock":
            print("Paper covers rock,won")
        else:
            print("Scissors cuts paper,lost.")

    elif my_choice == "scissors":
        if pc_choice == "paper":
            print("Scissors cuts paper,won")
        else:
            print("Rock smashes scissors,lost.")



    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break