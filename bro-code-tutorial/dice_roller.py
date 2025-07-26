import random

# Validate number of faces
while True:
    try:
        faces = int(input("How many faces does the die have? "))
        if faces <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

# Roll loop
while True:
    roll_or_no = input("Do you want to roll (Y/N)? ").upper()
    if roll_or_no == 'Y':
        print(random.randint(1, faces))
    elif roll_or_no == 'N':
        print("Thank you for playing!")
        break
    else:
        print("Invalid input! Please enter 'Y' or 'N'.")
