guess_number = 6
attempts = 5
guess = int(input("Guess the number"))
while guess != guess_number and attempts > 1:
    if guess < guess_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    attempts -= 1
    print(f"You have {attempts} attempts left")
    guess = int(input("Guess the number"))
    if attempts == 1 and guess != guess_number:
        print("You lost.Try again later")
        print()