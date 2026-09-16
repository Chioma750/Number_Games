import random
attempt = 0
max_attempt = 5

print("Choose your level")
print("Easy -> 1 to 100")
print("Medium -> 1 to 500")
print("Hard -> 1 to 1000")

print()
Level = input("Choose your level: ")

if Level.lower() == "easy":
    lower_bound = 1
    upper_bound = 100
elif Level.lower() == "medium":
    lower_bound = 1
    upper_bound = 500
elif Level.lower() == "hard":
    lower_bound = 1
    upper_bound = 1000

secret_number = random.randint(lower_bound, upper_bound)

while attempt < max_attempt:
    try:
        print()
        guess = int(input(f"guess a number from {lower_bound} to {upper_bound}: "))
    except:
        print("Invalid input, please input a valid number.")
        print()
        continue
    attempt += 1

    if guess == secret_number:
        print("You are correct ✅")
        print("you attempted", attempt, "times")
        break 
    elif attempt == max_attempt:
        print()
        print("You Failed 🤣")
        print("You have reached you limit!")
        print("The answer is", secret_number)
    elif guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
 