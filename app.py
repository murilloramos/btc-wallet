import os

private_key = os.urandom(32) # creates random secure number with 32 bytes
print(private_key.hex()) # .hex() is a function that converts an integer to a lowecase hexadecimal string

# This  will create a random secret number and print it on the console
