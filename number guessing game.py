secret = 27
max_attempts = 5
count = 0
guess = 0

print("=" * 42)
print("🎮 NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

while count < max_attempts and guess != secret:
    guess = int(input("Your guess: "))
    count += 1

    if guess == secret:
        print("Congratulations! You guessed the secret number!")
    else:
        if guess > secret:
            diff = guess - secret
        else:
            diff = secret - guess

        if diff >= 20:
            print("too far")
        elif diff >= 10:
            print("far")
        elif diff >= 5:
            print("closer")
        else:
            print("too close")

        remaining = max_attempts - count
        if remaining > 0:
            for i in range(remaining):
                print("❤️", end=" ")
            print()

if guess != secret:
    print("Game over")
    print("The secret number was:", secret)