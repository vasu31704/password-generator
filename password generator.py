import random
import string


def generate_password(length, letters, numbers, symbols):
    password =''
    if letters:
        password += string.ascii_letters
    if numbers:
        password += string.digits
    if symbols:
        password += string.punctuation

    if not password:
        print("Please select at least one character type.")
        return None

    seckey = ''.join(random.choice(password) for _ in range(length))
    return seckey


def passkey():
    print("which type of passkey do you want now ?")

    length = int(input("Enter the passkey length: "))

    letters = input(" letters? (1/0): ").lower() == '1'
    numbers = input(" numbers? (1/0): ").lower() == '1'
    symbols = input(" symbols? (1/0): ").lower() == '1'

    password = generate_password(length, letters, numbers, symbols)
    if password:
        print("Try this password:", password)


if __name__ == "__main__":
    passkey()
