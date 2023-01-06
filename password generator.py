import string
import random

def generate_password(length):
  # Get all uppercase and lowercase letters, digits, and special characters
  all_characters = string.ascii_letters + string.digits + string.punctuation
  # Generate a random password by selecting `length` characters from `all_characters` at random
  return ''.join(random.choice(all_characters) for i in range(length))

# Generate a password of length 20
password = generate_password(20)
print(password)
