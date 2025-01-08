import random

letterz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numberz = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbolz = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print ("Welcome to the PyPassword Generator!")
num_of_digits = int(input("How many letters would you like your password?\t"))

symbol = int(input("How many symbols would you like?\t\t"))
num = int(input("how many numbers would you like?\t\t"))
letters = int(input("how many letters would you like\t\t\t"))
password = []

for i in range(0,(num_of_digits + 1)):
    while (num>0):
        password.append(random.choice(numberz))
        num -= 

    while (letters>0):
        password.append(random.choice(letterz))
        letters -= 1
    
    while (symbol>0):
        password.append(random.choice(symbolz))
        symbol -= 1

shuffled_pass = ""

for x in range (0,num_of_digits+1):
    shuffled_pass += random.choice(password) 


print (f"Your password is {shuffled_pass}")

