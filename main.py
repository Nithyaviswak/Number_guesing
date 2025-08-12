secret_number = 7  # You can change this or use random.randint(1, 10)

print("Guess a number between 1 and 10:")
guess = int(input())

if guess == secret_number:
    print("🎉 Correct! You guessed the number.")
elif guess < secret_number:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")
