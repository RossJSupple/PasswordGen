import random

print("Welcome to your password generator")

def add():

    name = input("Account name: ")
    pwd = password

    with open('new_passwords.txt', 'a') as f:
        f.write(name + "/" + pwd  +"\n")

while True:

    start = input("Would you like to generate a password(yes or no)? ").lower()
    
    if start == "yes":

        chars = 'qwertyiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@£$%^&*()0123456789'
        num = int(input("How many passwords would you like? "))
        length = int(input("What length should the passwords be? "))
        for x in range (num):
            password = ''
            for y in range (length):
                password += random.choice(chars)
            cont = input("Would you like to add this to a file (yes or no)? ").lower()
            if cont == "yes":
                add()
            continue
    elif start == "no":
        break
print("Exiting...")
    