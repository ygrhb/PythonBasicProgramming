# Hardcoded secret number
secretnumber = 4
maxattemptnumbers = 10

# Collect player details
name = input("Enter your name: ")
print("Hello, " + name)
height = float(input("Enter your height: "))

# Track guesses in a list
guesses = []

# Boolean flag to control the game loop
still_playing = True

# Function to check guess and return result
def check_guess(secret, guess):
    if guess == secret:
        return "correct"
    elif guess > secret:
        return "high"
    else:
        return "low"

# First guess
numberinput = int(input("Enter a number between 1 and 10: "))

while still_playing:
    # Add guess to list
    guesses.append(numberinput)

    # Use our function to check the guess
    result = check_guess(secretnumber, numberinput)

    if result == "correct":
        print("Congratulations! You won!")
        still_playing = False

    else:
        maxattemptnumbers -= 1
        if result == "high":
            print("Too High! Try again.")
        elif result == "low":
            print("Too Low! Try again.")

        print("You have this many attempts remaining: " + str(maxattemptnumbers))

        if maxattemptnumbers == 0:
            print("Sorry, you lose!")
            still_playing = False
        else:
            numberinput = int(input("Enter a number between 1 and 10: "))

# Print all guesses with a for loop
print("\nYour guesses were:")
for guess in guesses:
    print(guess)
