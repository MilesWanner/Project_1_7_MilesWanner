"""
Program: Python Automotive Quiz
Author: Miles Wanner
Date: 6/18/2026
Purpose: A command-line quiz game that tests new automotive recruits on vehicle makes and body types.
Resources: Python Crash Course (Chapters 1-7)
"""



print("Welcome to Python Automotive!")

print("\nYou are the manager of the #1 automotive shop in Central Ohio. However, the recruits struggle to identify basic cars. Your task is to assess and reinforce new employees' knowledge of vehicle makes and body types. First, you will be quizzed to assess your own vehicle knowledge. Later, each recruit will be tested in the same way, so they are prepared to identify the right tools for the job.")

vehicles = {
    'Accord': {
        'make': "Honda",
        'body': "Sedan"
    },
    'Explorer': {
        'make': "Ford",
        'body': "SUV"
    },
    'Prius': {
        'make': "Toyota",
        'body': "Hatchback"
    },
    'Pacifica': {
        'make': "Chrysler",
        'body': "Minivan"
    },
    'Silverado': {
        'make': "Chevrolet",
        'body': "Truck"
    }
}

print("\nHere is the common vehicle list:")
for vehicle in vehicles:
    print(f"{vehicle}")

instructions = "\nFirst, you will be quizzed to test your own vehicle knowledge"
instructions += "\nTo start, first choose a model from the list: "

user_vehicle = input(instructions)

while user_vehicle not in vehicles:
    print("\nSorry, that vehicle is not in the list!")
    user_vehicle = input(instructions)

user_make = vehicles[user_vehicle]['make']
user_body = vehicles[user_vehicle]['body']

strikes = 3

while strikes > 0:
    round_one = "The first round will involve identifying the car's make."
    round_one += "\nGuess the make of your chosen vehicle: "

    guess_make = input(round_one)

    if guess_make.title() == user_make:
        print("You guessed the correct make!")

        round_two = "The second round will involve identifying the car's body type."
        round_two += "\nGuess the body type of your chosen vehicle: "

        guess_body = input(round_two)

        if guess_body.title() == user_body:
            print ("You guessed the correct body type!")
            print("\nCongrats! You WON the game!")
            break
        else:
            print("You did not guess the correct body type!")
            strikes = strikes - 1
            print(f"\nYou have {strikes} remaining.")
    elif guess_make == "":
        print("\nYou must enter a guess!")
    else:
        print("You did not guess the correct make!")
        strikes = strikes - 1
        print(f"\nYou have {strikes} remaining.")

if strikes == 0:
    print("\nSorry! You LOST the game.")
