import random

name = input("Hello, what's your name: ")

print(
    "Hello " + name + ", Let's start the game!\n"
                      "I'm selecting a number between 1 and 10. You have to guess which one is it.\n"
                      "Remember: You only have 5 attempts!")

answer = random.randint(1, 10)

attempts = 1

while (attempts <= 5):
    response = int(input("Guess " + str(attempts) + ":"))

    if (response == answer):
        print("You guessed right, the selected number was " + str(answer) + "!")
        break
    elif (response > answer):
        print("Your number was high")
    else:
        print("Your number was low")

    attempts = attempts + 1
