import random

user = int(input("Enter the lenght of the password you want to be: "))

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"

password = "".join(random.sample(characters,user))

print(f"Your password is: {password}")