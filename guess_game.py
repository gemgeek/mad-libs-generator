import random

def play_game():
    secret_number = random.randint(1, 10)
    guess_count = 0

    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        try:
            guess = int(input("Your guess: "))
            guess_count += 1

            match guess:
                case x if x == secret_number:
                    print(f"🎉 Congratulations, you guessed it in {guess_count} tries!")
                    break
                case x if x > secret_number:
                    print("📈 Oops, your guess is a bit high. Try again!")
                case x if x < secret_number:
                    print("📉 Nope, your guess is a bit low. Give it another shot!")
        except ValueError:
            print("❗Please enter a valid number.")

    # Ask if they want to play again
    again = input("🔁 Play again? (yes/no): ").lower()
    if again == "yes":
        play_game()
    else:
        print("👋 Thanks for playing! See you next time.")

# Start the game
play_game()
