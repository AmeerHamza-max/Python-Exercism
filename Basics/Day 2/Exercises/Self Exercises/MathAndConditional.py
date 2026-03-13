import math
# # 1
# num1=int(input("Enter first Number : "))
# num2=int(input("Enter Second Number : "))
# print(f"Sum of two numbers {num1} + {num2} = {num1+num2} ")

# # 2
# print(f"Difference of two numbers {num1} - {num2} = {num1-num2}")
# # 3
# print(f"Product of two numbers {num1} * {num2} = {num1*num2}")
# # 4
# print(f"Division of two numbers {num1}/{num2} = {num1/num2}")

# # 5
# print(f"Square of number {num1} = {pow(num1,2)}")
# # 6
# print(f"Cube of number {num1} = {num1**3}")

# # 7
# if num1%2==0:
#     print(f"{num1} is an even number")

# else:
#     print(f"{num1} is an odd number")

# # 8
# if(num1>0):
#     print(f"{num1} is a positive number")

# elif(num1<0):
#     print(f"{num1} is a negative number")
# else:
#     print(f"{num1} is a zero ")

# # 9

# if(num1%5==0):
#     print(f"{num1}Divisible by 5")
# # 10
# if(num1%3==0):
#     print(f"{num1} divisible by 3")

# # 11

# if(num1>num2):
#     print(f"{num1} is greater then {num2}")
# else:
#     print(f"{num2} is greater then {num1}")

# # 12
# if(num1<num2):
#     print(f"{num1} is less then the {num2}")
# else:
#     print(f"{num2} is less then the {num1}")

# # 13
# num3=int(input("Enter the third number: "))
# if(num1>num2 and num1>num3):
#     print("{num1} is greater then the numbers {num2} and {num3}")
# elif num2>num1 and num2>num3:
#     print("{num2} is greater then the numbers {num1} and {num3}")
# elif num3>num1 and num3>num2:
#     print("{num3} is greater then the numbers {num1} and {num2}")

# # 14
# if(num1<num2 and num1<num3):
#     print(f"{num1} is less then the numbers {num2} and {num3}")
# elif num2<num1 and num2<num3:
#     print(f"{num2} is less then the numbers {num1} and {num3}")
# elif num3<num1 and num3<num2:
#     print(f"{num3} is less then the numbers {num1} and {num2}")

# # 15
# age=int(input("Enter age: "))
# if(age>=18):
#     print(f"Age is {age} you are eligible to vote.")
# else:
#     print(f"Age is {age} you are not eligible to vote.")

# # 16
# if(num3%10==0):
#     print(f"{num3} is a multiple of 10")
# else:
#     print(f"{num3} is not a multiple of 10")

# # # 17

# num1=108
# if(num1 >= 1 and num1 < 9):
#     print(f"{num1} is a 1 digit number")
# elif(num1 >=10 and num1 <99):
#     print(f"{num1} is a 2 digit number")
# elif(num1 >= 100 and num1 <=999):
#     print(f"{num1} is a 3 digit number")

# # 18
# num1=45
# num2=50
# if num1==num2:
#     print(f"{num1} and {num2} are equal")
# else:
#     print(f"{num1} and {num2} are not equal")

# 19
num1=23
if(num1%3==0):
    print(f"{num1} is divisible by 3")
elif (num1%5==0):
    print(f"{num1} is divisible by 5")
else:
    print(f"{num1} is divided by some else not 5 nor 3")

# 20
num1=111
if num1 > 100:
    print(f"{num1} is greater then 100")
else:
    print(f"{num1} is not greater than 100")

# 21
n=19
for i in range(2,6):
    if i%n==0:
        print("{n} this not a prime num")
    else:
        print(f"{n}  is a prime number")
        break

# 22
num1=6
if num1==math.sqrt(num1)*math.sqrt(num1):
    print(f"{num1} is a perfect square of {math.sqrt(num1)}")
else:
    print(f"{num1} is not a perfect square ")

# 23
num1=22
num2=11
num3=34
if  (not num1 < num2 and   num1 < num3) and (not num1 > num2 and  not num1 < num3):
    print(f"{num1} is  in between {num2} and {num3}")
elif  (not num2 < num1 and   num2 < num3) and (not num1 > num2 and  not num1 < num3):
    print(f"{num1} is  in between {num2} and {num3}")

    
    

