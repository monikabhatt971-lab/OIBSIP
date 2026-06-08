# Oasis Infobyte Internship - Task 3: Random Password Generator
# Created by: Monika Bhatt 

import random
import string

print("===Welcome to the oasis infobyte Password Generator===")

try:
    length = int(input("Enter the desired password length:"))

    if length < 4:
        print("Error: Password length should be at least 4 characters for better security.")
    else:
        letters = string.ascii_letters #a-z,A-Z
        numbers = string.digits #0-9
        symbols = string.punctuation #!,@,#,$,etc.

        all_characters = letters + numbers + symbols

        password_list = [
            random.choice(letters),
            random.choice(numbers),
            random.choice(symbols)
        ]

        for _ in range(length - 3):
             
            password_list.append(random.choice(all_characters))

        random.shuffle(password_list)

        generated_password ="".join(password_list)

        print("\n----------------------------------")
        print(f"Your Generated Password is: {generated_password}")
        print("----------------------------------")

except ValueError:
     print("Error:Please enter a valid number for password length.")

print("\n Thank you for using the Password Generator!")