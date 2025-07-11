import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# my version
random_letters = random.choices(letters,k = nr_letters)#here choose a random letter list based on user input
letter = ""

for l in random_letters:
    letter += l

random_symbols = random.choices(symbols,k =nr_symbols)
symbol = ""

for s in random_symbols:
    symbol += s

random_numbers = random.choices(numbers,k = nr_numbers)
number =""

for n in random_numbers:
    number += n


password = letter+symbol+number

random_password = ''.join(random.sample(password,len(password)))
print(f"Your password is : {random_password}")
#video version
## Easy Version
# password =""
#
# for char in range(0, nr_letters):
#      password += random.choice(letters)
#
# for sym in range(0, nr_letters):
#      password += random.choice(symbols)
#
# for num in range(0, nr_letters):
#      password += random.choice(numbers)
#
# print(password)

## Hard Version
# password_list =[]
# 
# for char in range(0, nr_letters):
#      password_list.append(random.choice(letters))
# 
# for sym in range(0, nr_letters):
#      password_list.append(random.choice(symbols))
# 
# for num in range(0, nr_letters):
#      password_list.append(random.choice(numbers))
# 
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
# password =""
# for i in password_list:
#      password += i
# print(f"Your password is : {password}")
