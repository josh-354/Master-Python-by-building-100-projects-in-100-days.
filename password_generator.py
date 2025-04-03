import random

letter = ['a', 'X', 'p', 'J', 'z', 'M', 'c', 'L', 'e', 'Q']
symbol = ['@', '#', '$', '%', '&', '*', '!', '?', '/', '+']
numbers = ['3', '7', '1', '9', '4', '6', '2', '0', '8', '5']


nr_letters = int(input("How many letters you want"))
nr_symbol = int(input("How many symbol you want"))
nr_number = int(input("How many number you want"))


password_list=[]

for char in range(0,nr_letters):
    password_list.append(random.choice(letter))

for char in range(0,nr_number):
    password_list.append(random.choice(numbers))

for char in range(0,nr_symbol):
    password_list.append(random.choice(symbol))


print(password_list)
random.shuffle(password_list)


password=""
for i in password_list:
    password+=i

print(f"your password is {password}")
    
