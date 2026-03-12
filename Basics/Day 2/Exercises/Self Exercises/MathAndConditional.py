import math
# 1
num1=int(input("Enter first Number : "))
num2=int(input("Enter Second Number : "))
print(f"Sum of two numbers {num1} + {num2} = {num1+num2} ")

# 2
print(f"Difference of two numbers {num1} - {num2} = {num1-num2}")
# 3
print(f"Product of two numbers {num1} * {num2} = {num1*num2}")
# 4
print(f"Division of two numbers {num1}/{num2} = {num1/num2}")

# 5
print(f"Square of number {num1} = {pow(num1,2)}")
# 6
print(f"Cube of number {num1} = {num1**3}")

# 7
if num1%2==0:
    print(f"{num1} is an even number")

else:
    print(f"{num1} is an odd number")

# 8
if(num1>0):
    print(f"{num1} is a positive number")

elif(num1<0):
    print(f"{num1} is a negative number")
else:
    print(f"{num1} is a zero ")

# 9

if(num1%5==0):
    print(f"{num1}Divisible by 5")
# 10
if(num1%3==0):
    print(f"{num1} divisible by 3")

# 11

if(num1>num2):
    print(f"{num1} is greater then {num2}")
else:
    print(f"{num2} is greater then {num1}")

# 12
if(num1<num2):
    print(f"{num1} is less then the {num2}")
else:
    print(f"{num2} is less then the {num1}")

# 13
num3=int(input("Enter the third number: "))
if(num1>num2 and num1>num3):
    print("{num1} is greater then the numbers {num2} and {num3}")
elif num2>num1 and num2>num3:
    print("{num2} is greater then the numbers {num1} and {num3}")
elif num3>num1 and num3>num2:
    print("{num3} is greater then the numbers {num1} and {num2}")

# 14
if(num1<num2 and num1<num3):
    print(f"{num1} is less then the numbers {num2} and {num3}")
elif num2<num1 and num2<num3:
    print(f"{num2} is less then the numbers {num1} and {num3}")
elif num3<num1 and num3<num2:
    print(f"{num3} is less then the numbers {num1} and {num2}")

# 15
age=int(input("Enter age: "))
if(age>=18):
    print(f"Age is {age} you are eligible to vote.")
else:
    print(f"Age is {age} you are not eligible to vote.")

# 16
if(num3%10==0):
    print(f"{num3} is a multiple of 10")
else:
    print(f"{num3} is not a multiple of 10")

# 17

