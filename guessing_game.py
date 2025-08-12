secret_number = 7
attempts = 5

print("=== Number Guessing Game ===")
print(f"You have {attempts} attempts to guess the number between 1 and 10.")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))

    if guess == secret_number:
        print("🎉 Correct! You guessed it.")
        break
    elif guess < secret_number:
        print("📉 Too low! Try a bigger number.")
    else:
        print("📈 Too high! Try a smaller number.")
else:
    print("❌ Game Over! The number was", secret_number)
