import random
secret_number = random.randint(1, 100)
attempt = 0
max_attempt = 5

while attempt < max_attempt:
    guess = int(input("guess a number from 1 to 100: "))
    attempt += 1
    
    if guess == secret_number:
        print("You are correct ☺️")
        print("you attempted", attempt, "times")
        break 
    elif attempt == max_attempt:
        print("You Failed 🤣")
        print("The answer is", secret_number)
    elif guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
 