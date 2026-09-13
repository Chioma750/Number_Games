import random
secret_number = random.randint(1, 100)
attempt = 0

while True:
    guess = int(input("guess a number from 1 to 100: "))
    attempt += 1
    
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    elif guess == secret_number:
        print("You are correct")
        print("you attempted", attempt, "times")
        break 
    else:
        continue
 
