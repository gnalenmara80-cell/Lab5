"""
Lab 5 - Dice Rolling Terms
Author: Gnalen Mara
Purpose: This code writes a program that rolls two dice, prints the outcome,
and then uses conditional statements to print the appropriate term for that roll.
Date: 02/13/2026
"""

import random

def get_term(d1, d2, total):
    if d1 == 1 and d2 == 1:
        return "Snake Eyes"
    elif (d1 == 1 and d2 == 2) or (d1 == 2 and d2 == 1):
        return "Ace Cought a Deuce"
    elif d1 == 2 and d2 == 2:
        return "Little Joe from Kokomo"
    elif (d1 == 1 and d2 == 4) or (d1 == 4 and d2 == 1):
        return "Little Phoebe"
    elif d1 == 3 and d2 == 3:
        return "Jimmy Hicks from the Sticks"
    elif (d1 == 6 and d2 == 1) or (d1 == 1 and d2 == 6):
        return "Six Ace"
    elif d1 == 4 and d2 == 4:
        return "Eighter from Decatur"
    elif (d1 == 3 and d2 == 6) or (d1 == 6 and d2 == 3):
        return "Nina from Pasadena"
    elif d1 == 5 and d2 == 5:
        return "Puppy Paws"
    elif (d1 == 6 and d2 == 5) or (d1 == 5 and d2 == 6):
        return "Six Five No Jive"
    elif d1 == 6 and d2 == 6:
        return "BoxCars"
    else:
        return "No special term"


print("Welcome to the dice roll term generator!")

while True:
    input("Press Enter to roll the dice...")

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    print(f"\nYou rolled a {die1} and a {die2}")
    print(f"Total: {total}")

    term = get_term(die1, die2, total)
    print(f"Term: {term}")

    again = input("\nRoll again? (y/n): ").lower()
    if again != "y":
        print("Goodbye!")
        break