import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")

password_list = []

no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_numbers = int(input("How many numbers would you like?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))

for letter in range(1 , no_of_letters + 1) :
    password_list.append(random.choice(letters))
for number in range(1, no_of_numbers + 1) :
    password_list.append(random.choice(numbers))
for symbol in range(1 , no_of_symbols + 1) :
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

#print(password_list)

password = ""

for char in password_list :
    password += char

print("Your password is " + password)