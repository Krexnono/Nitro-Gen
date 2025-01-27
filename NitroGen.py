import time
import random
import string
import os

os.system('clear')

def generate_random_string(length=16):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

try:
    num_nitro = int(input("Combien de Nitro ? : "))
    for i in range(1, num_nitro + 1):
        random_string = generate_random_string()
        print(f"https://discord.com/gifts/{random_string} ({i}) ")
        time.sleep(0.05)
except ValueError:
    print("Veuillez entrer un nombre valide.")