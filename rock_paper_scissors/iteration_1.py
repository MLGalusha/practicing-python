import random

# print title
print("\nLets play rock paper scisors!")

# Specify choice options
options = ["r", "p", "s"]


# Create a continuous loop that takes user input
while True:
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ").lower()
    print(' ')

    # check if user input is in options
    if user_choice in options:

        # have computer select random choice out of options
        computer_choice = random.choice(options)

        mapping = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

        def convert_choice(choice):
            return mapping.get(choice)

        # Make it easier to tell the user both of the choices.
        choices = f"You chose: {convert_choice(user_choice)}\nComputer chose: {convert_choice(computer_choice)}"

        # Checks if both choices are equal
        if user_choice == computer_choice:
            print(f"You both chose {convert_choice(user_choice)}.\nIt's a tie!")

        # If not equal check who won and who lost.
        else:
            match user_choice:
                case 'r':
                    match computer_choice:
                        case 'p':
                            print(f"You lost!\n{choices}")
                        case 's':
                            print(f"You win!\n{choices}")
                case 'p':
                    match computer_choice:
                        case 's':
                            print(f"You lost!\n{choices}")
                        case 'r':
                            print(f"You win!\n{choices}")
                case 's':
                    match computer_choice:
                        case 'r':
                            print(f"You lost!\n{choices}")
                        case 'p':
                            print(f"You win!\n{choices}")

        # Ask the user if they want to play again and restart program or end it based on users response.
        print("\nWould you like to play again?")
        play_again = input("Type (y) to continue or anything else to exit. ")
        if play_again.lower() != 'y':
            break

    else:
        print("Invalid input. type either r, p, s. for rock paper scissors.")

print("Thank you for playing Rock Paper Scissors. See you next time!\n")



