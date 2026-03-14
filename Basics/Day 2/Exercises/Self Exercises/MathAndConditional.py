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
num1=34
num2=11
num3=22
if  (not num1 < num2 and  not num1 > num3) or (not num1 < num3 and not num1 > num2):
    print(f"{num1} this is num 1 in between {num2} and {num3}")
elif  (not num2 < num1 and   not num2 > num3) or (not num2 < num3 and not num2 > num1):
    print(f"{num2}  this is num 2  in between {num1} and {num3}")

elif  (not num3 < num1 and   not num3 > num2) or (not num3 < num2 and not num3 > num1) :
    print(f"{num3}  this is num 3  in between {num1} and {num2}")

# 24

num4=int(input("Enter a number :"))
if(num4 >=10 and num4 <=50):
    print(f"Yes {num4} is in between 10 and 50")
else:
    print(f"Yes {num4} is in between 10 and 50")
    
 
# 25
p=50000
r=6000
t=3
I=p*r*t
print(f"The total Interest Rate : {I}")

# 26
marks=int(input("Enter Your Marks : "))
if(marks >=90):
    print("A grade")
elif(marks >=80 and marks < 90):
    print("B grade")
elif(marks >=70 and marks < 80):
    print("C grade")
elif(marks >=60 and marks < 70):
    print("D grade")
else:
    print("You are Fail")

# 27

num1=int(input("Enter a number to check it is divisible by 2 , 3 or both : "))

if(num1%2==0 and num3%2==0):
    print(f"{num1} it is divisible by both 2 and 3")
elif num1%2==0:
    print(f"{num1} is only divisible by 2")
elif num1%3==0:
    print(f"{num1} is only divisible by 3")
else:
    print(f"{num1} is not divisible by 2 nor 3")

# 28

if(num1+num2>num3):
    print(f"{num1} {num2} {num3}They form a trinagle")

elif(num2+num3>num1):
    print(f"{num1} {num2} {num3}They form a trinagle")
elif(num2+num3>num1):
    print(f"{num1} {num2} {num3}They form a trinagle")
elif(num1+num3>num2):
    print(f"{num1} {num2} {num3} They form a trinagle")
else:
     print(f"{num1} {num2} {num3}They form a trinagle")
# 29
year=2004
if(year%4==0):
    print("This is a leap year")
else:
    print("This is not a leap year")

# 30
temp=30

if(temp>=20 and temp<=30):
    print("Warm outside")
elif(temp<0):
    print("Cold Outside")
elif(temp>30):
    print("Hot outside")

# 31
num1=int(input("Enter a number to check it is divisible by 2 , 3 or both : "))

if(num1%7==0 and num3%11==0):
    print(f"{num1} it is divisible by both 2 and 3")
elif num1%7==0:
    print(f"{num1} is only divisible by 2")
elif num1%11==0:
    print(f"{num1} is only divisible by 3")
else:
    print(f"{num1} is not divisible by 2 nor 3")


# 32
if(num1 >=1 and num1 <=100):
    print(f"{num1} is in range between 1 to 100")

# 33
if(num1%num2==0):
    print(f"{num1} completely divides on {num2}")
else:
    print(f"{num1} does not completely divide on {num2} ")

# 34
if((num1 > 10 and num1 <100 ) and num1%2==0):
    print(f"{num1} is a two digit even number ")
else:
    print(f"{num1} is not a two digit even number")

# 35
salary=int(input("Enter your salary = "))
if(salary==600000):
    print(f"{salary} no tax in pakistan")
elif(salary>600000 and salary<=1200000):
    print(f"{salary} before tax deduction")
    salary=(salary*2.5)/100
    print(f"{salary}  salary after tax deduction")
elif(salary>1200000 and salary<=2200000):
    print(f"{salary} before tax deduction")
    salary=(salary*11)/100
    print(f"{salary}  salary after tax deduction")
elif(salary>2200000 and salary<=2200000):
    print(f"{salary} before tax deduction")
    salary=(salary*23)/100
    print(f"{salary}  salary after tax deduction")
elif(salary>2200000 and salary<=3200000):
    print(f"{salary} before tax deduction")
    salary=(salary*23)/100
    print(f"{salary}  salary after tax deduction")
elif(salary>3200000 and salary<=4100000):
    print(f"{salary} before tax deduction")
    salary=(salary*30)/100
    print(f"{salary}  salary after tax deduction")
elif( salary>4100000):
    print(f"{salary} before tax deduction")
    salary=(salary*35)/100
    print(f"{salary}  salary after tax deduction")
    
else:
    print("No tax")

# 36
days=8317
print(f"Number of days {days} in weeks {math.floor(days/7)}")
print(f"Number of remainig days after weeks {math.floor(days%7)}")

# 37
if(num1%2==0 and num2%2==0):
    print(f"{num1} and {num2} both are even")
else:
    print(f"No {num1} and {num2} both are not even")

# 38
if(num1%9==0):
    print(f"{num1} is perfectly divisible by 9")
else:
    print(f"{num1} not perfectly divisible by 9")

# 40
if(num1 >50 and num1 < 100):
    print(f"{num1} is greater than 50 and less then 100")
else:
    print(f"{num1} is not in range between 50 and 100")


# 41
num1=34
num2=11
num3=22

print(f"{num1},{num2} and {num3} ")




if(num1<num2 and num1<num3):
    print(num1)
elif(num2<num1 and num2<num3):
    print(num2)
elif(num3<num2 and num3<num1):
    print(num3)
else:
    print('All numbers all equal')


if  (not num1 < num2 and  not num1 > num3) or (not num1 < num3 and not num1 > num2):
    print(f"{num1}")
elif  (not num2 < num1 and   not num2 > num3) or (not num2 < num3 and not num2 > num1):
    print(f"{num2}")

elif  (not num3 < num1 and   not num3 > num2) or (not num3 < num2 and not num3 > num1) :
    print(f"{num3}")



if(num1>num2 and num1>num3):
    print(num1)
elif(num2>num1 and num2>num3):
    print(num2)
elif(num3>num2 and num3>num1):
    print(num3)
else:
    print("All numbers are equal")

# 42
num1=34
num2=11
num3=22

print(f"{num1},{num2} and {num3} ")

if(num1>num2 and num1>num3):
    print(num1)
elif(num2>num1 and num2>num3):
    print(num2)
elif(num3>num2 and num3>num1):
    print(num3)
else:
    print("All numbers are equal")

if  (not num1 < num2 and  not num1 > num3) or (not num1 < num3 and not num1 > num2):
    print(f"{num1}")
elif  (not num2 < num1 and   not num2 > num3) or (not num2 < num3 and not num2 > num1):
    print(f"{num2}")

elif  (not num3 < num1 and   not num3 > num2) or (not num3 < num2 and not num3 > num1) :
    print(f"{num3}")


if(num1<num2 and num1<num3):
    print(num1)
elif(num2<num1 and num2<num3):
    print(num2)
elif(num3<num2 and num3<num1):
    print(num3)
else:
    print('All numbers all equal')

num4=56

# 43
if(num1>num2 and num1>num3 and num1>num4):
    print(num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print(num2)
elif(num3>num2 and num3>num1 and num3>num4):
    print(num3)
elif(num4>num1 and num4>num2 and num4>num3):
    print(num4)
else:
    print("All numbers are equal")

    
# 44
num1="341"
n1=(pow(int(num1[0]),3))
n2=int(pow(int(num1[1]),3))
n3=int(pow(int(num1[2]),3))
if(n1+n2+n3==int(num1)):
    print(f"{num1} is an Armstrong number ")
else:
    print(f"{num1} is not an Armstrong number")


# 45
first="1221"
palindrom=first[::-1]
if(palindrom==first):
    print(f"{first} is a palindrom")
else:
    print(f"{first} is not a palindrom")


# 46
sum=0
perfect=6
if(perfect%1==0):
    sum=sum+1
if(perfect%2==0):
    sum=sum+2
if(perfect%3==0):
    sum=sum+3
if(perfect%4==0):
    sum=sum+4
if(perfect%5==0):
    sum=sum+5
print(sum)

if(sum==perfect):
    print(f"{perfect} is a perfect number")
else:
    print(f"{perfect} is not a perfect")


# 47
side1=60
side2=60
side3=90
if(side1==side2==side3):
    print("This is an equilateral triangle")
elif(side1==side2  or side2==side3 or side1 == side3):
    print("This is Isosceles")
elif(side1 !=side2 !=side3):
    print("This is Scalne")
