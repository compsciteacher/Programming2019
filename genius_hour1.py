# Create a program that adds together two random numbers between 1 and 100, then prints the total.
# Print the square root of a random number between 1 and 100.
# I attached a link for the math module (pretty simple stuff)

import random,math

num1=random.randint(1,100)
num2=random.randint(1,100)
print(num1+num2)

#--------------------

num3=random.randint(1,100)
print(math.sqrt(num3))

#-----doing these each multiple times to see them

for i in range(10):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(num1 + num2)

for x in range(10):
    num3 = random.randint(1, 100)
    print(math.sqrt(num3))
    