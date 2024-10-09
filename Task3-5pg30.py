#Author: Kacper Trela
#Date: Oct 2024
#Pg 30 Task 3-5

#Task 3

# cost = int(input("How much does item cost: ")) #Gets the price of the item
# 
# if cost > 10000: #If cost is over 10000 print the message
#     print("Price too high, please go to tender")
# elif cost >= 500: #If price is higher or equal to 500 prints the message
#     print("Get quotes from 3 different suppliers")
# elif cost < 500: #If price is less than 500 prints message
#     print("Order now!")


#Task 4


option = input("You've won a free tram ticket! Please pick an option; A, B or C: ").upper() # input your option

if option == "A": # if the variable option is equal to A print the message
    print("You have won a free ticket to Dundrum Shopping Centre.")
elif option == "B": # if the variable option is equal to B print the message
    print("You have won a free ticket to Tallaght.")
elif option == "C": # if the variable option is equal to C print the message
    print("You have won a free ticket to Broombridge.")
else: # if the variable does not eqaul to A, B or C print the message
    print("Invalid Input")

# Task 5

mark = int(input("Enter your marks:"))

if mark <= 29:
    print("H8")
elif mark <= 39:
    print("H7")
elif mark <= 49:
    print("H6")
elif mark <= 59:
    print("H5")
elif mark <= 69:
    print("H4")
elif mark <= 79:
    print("H3")
elif mark <= 89:
    print("H2")
elif mark <= 100:
    print("H1")
    
