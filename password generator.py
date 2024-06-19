import string
import random
import time

print("Hello! Here are your passwords sir:")

def generate_password(length):
    safe_special_characters = "!#$%&*+-=?@^_"
    all_characters = string.ascii_letters + string.digits + safe_special_characters
    return ''.join(random.choice(all_characters) for i in range(length))

for i in range(20):
    time.sleep(0.3)
    password = generate_password(20)
    print(password)

input("Press Enter to exit...")
