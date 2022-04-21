#Random password generator
#Don't make your password too long
#I think, 20 characters will be ok :)

import random

print("The random password generator.")
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?_+"
password_len = int(input("How many characters in your password do you want: "))
password = ""
y = len(characters)
for x in range(password_len):
    password += characters[random.randint(1, y)]
print("Here's your new password:", password)
