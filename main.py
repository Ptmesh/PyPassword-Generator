import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator")

numOfLetters = int(input("How many letters would you like to have in your password? \n"))
numOfSymbols = int(input("How many sybmols would you like to have in your password? \n"))
numOfNumber = int(input("How many numbers would you like to have in your password? \n"))

password =[]

for char in range(1 , numOfLetters + 1):
    password.append(random.choice(letters))
for sym in range(1 , numOfSymbols + 1):
    password.append(random.choice(symbols))
for num in range(1, numOfNumber + 1):
    password.append(random.choice(numbers))
random.shuffle(password)

newPassword = ""
for key in password:
    newPassword += key

print(f"Your freshly generated password is: {newPassword}")
