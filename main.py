import random
secret_number = random.randint(1, 100)

guess = int(input("guess a number from 1 to 100: "))

while True:
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("You are correct") 
        if guess != secret_number:
            continue
        else:
            break   
