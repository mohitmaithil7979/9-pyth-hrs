import random

user_guess = input("Type a number: ")
if user_guess.isdigit():
    user_guess = int(user_guess)
    if user_guess <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, user_guess)
print( random_number )


random_number = random.randint(0, user_guess)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

print("You got it in", guesses, "guesses")