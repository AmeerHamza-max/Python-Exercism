# 1
name=input('Enter your name: ')
print(name)
# 2
age=input("Enter your age: ")
print(age)
# 3
city=input("Enter your city: ")
print(city)
# 4
color=input("Enter your favourite color: ")
print(color)
# 5
color=int(input("Enter a number input: "))
print(color)
# 6
num1=input("Enter first number: ")
num2=input("Enter Second Number")
print(f"Sum of two numbers {num1} + {num2} = {int(num1)+int(num2)}")
# 7
num3=int(input("Enter a number to take it's square: "))
print(f"Square of {num3} is = {num3*num3}")
# 8
num4=int(input("Enter a radius to calculate the circle area : "))
pi=3.14
print(f"Area of circle is having radius {num4} is = {pi*num4*num4}")

# 9 
length=int(input("Enter the length : "))
width=int(input("Enter the width : "))
print(f"The area of rectangle containing {length} and {width} is = {(length*width)*1/2}")


# 10
num5=int(input("Enter first  number : "))
num6=int(input("Enter second number : "))
num7=int(input("Enter third number : "))
print(f"The average of three numbers {num5} {num6} {num7} = {(num5 + num6 + num7)/3}")


# 11
num8=int(input("Enter a number to check it is even or odd"))
num9=num8%2==0
num10=num8%2!=0
if(num9):
    print(f"{num8}  {num9} this is even")
else:
    print(f"{num8} {num10} this is odd")
# 12
age1=int(input("Enter the age : "))
if(age1>18):
    print('You are an adult')
else:
    print("You are not an adult")
# 13
temp=int(input("Enter temprature in degree centigrade : "))
print (f"Temprature in farenheit {9/5*(temp+32)}")
# 14
marks=int(input("Enter your marks "))
print(f'Percentage of a student : {(marks*100)/505}')
# 15
num10=int(input("Enter first number : "))
num11=int(input("Enter second number : "))
if(num10>num11):
    print(f"{num10} is greater then {num11}")
else:
    print(f"{num11} is greater then {num10}")
