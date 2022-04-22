#Random password generator v.2

#Last version could make an error:
#IndexError: string index out of range
#   and run correct of the same value of password_len.
#I have no idea, why it can work or can't work for the same condition.
#Now - it works, if your password has less characters than 75
#   ('cause string characters has 75 marks)

import random

print("The random password generator.")
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?_+"
password_len = int(input("How many characters in your password do you want: "))
password = ""
y = len(characters)
for x in range(password_len):
    password = "".join(random.sample(characters, password_len))
print("Here's your new password:", password)
