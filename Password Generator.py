import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range (length))
    return password
# User input
while True:
    try:
        length = int(input("Enter password length:  "))
        if length <1:
            print ("Length must be at least 1.")
            continue
        break
    except ValueError:
        print ("Please enter a valid number.")

# Generate and show password
new_password = generate_password(length)
print("Generated Password:", new_password)