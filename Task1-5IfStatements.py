# Author: Kacper Trela
# Date: Oct 2024
# If Statement Exercises Q1 -Q5

# Task 1

# name = input("What is your name?:" )
# 
# if len(name) < 7:
#     print("Hello "+name+"! Your name is short.")
# elif len(name) <= 10:
#     print("Hello "+name+"! Your name is long.")
# elif len(name) > 10:
#     print("Hello "+name+"! Your name is very long.")
    
# Task 2
# print("Menu")
# print("1. Music")
# print("2. History")
# print("3. Design and Technology")
# print("4. Exit")
# 
# choice = int(input('Please enter your choice:'))
# 
# if choice == 1:
#     print('You chose Music')
# elif choice == 2:
#     print('You chose History')
# elif choice == 3:
#     print('You chose Design and Technology')
# elif choice == 4:
#     print('Goodbye')
# else:
#     print('Invalid Option')

# Task 3
# import random
# 
# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)
# dicesum = dice1 + dice2
# dicemult = dice1 * dice2
# 
# print(dice1, dice2)
# 
# if dice1 != dice2:
#     print("Your score =" ,dicesum)
# if dice1 == dice2:
#     print("Your score =" ,dicemult)

# Task 4

# price = float(input("Price of the product?:"))
# 
# if price >= 200:
#     print('Your goods would cost',price,'but with the 10% discount they cost,',(price/100)*90)
# elif price >= 100:
#     print('Your goods would cost',price,'but with the 5% discount they cost,',(price/100)*95)
# elif price < 100:
#     print("No discount given. Sorry")
    
# Task 5

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

if num1 > num2:
    out = num1 - num2
else:
    out = num2 - num1

print("The differnce is", out)

    
