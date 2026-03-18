print(2 + 3 * 3)
print((2 + 3) * 3)


height = 172.5
weight = 68.55

# the Body Mass Index, or BMI, is calculated by dividing body mass with the square of height
# height is converted into metres in the formula
bmi = weight / (height / 100) ** 2

print(f"The BMI is {bmi}")


x = 3
y = 2

print(f"/ operator {x/y}")
print(f"// operator {x//y}")



input_str = input("Which year were you born? ")
year = int(input_str)
print(f"Your age at the end of the year 2021: {2021 - year}" )



year = int(input("Which year were you born? "))
print(f"Your age at the end of the year 2021: {2021 - year}" )


height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

height = height / 100
bmi = weight / height ** 2

print(f"The BMI is {bmi}")



# exercise 2
# Write your solution here
num1=int(input("Please type in a number:"))
print(f"{num1} times 5 is {num1*5}")

# # Write your solution here

name=input("What is your name?")
year=int(input("Which year were you born?"))
print(f"Hi {name}, you will be {2021-year} years old at the end of the year 2021")



number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

sum = number1 + number2 + number3
print(f"The sum of the numbers: {sum}")


sum = 0

number = int(input("First number: "))
sum = sum + number

number = int(input("Second number: "))
sum = sum + number

number = int(input("Third number: "))
sum = sum + number

print(f"The sum of the numbers: {sum}")



sum = 0

sum += int(input("First number: "))
sum += int(input("Second number: "))
sum += int(input("Third number: "))

print(f"The sum of the numbers: {sum}")


number1 = int(input("First number: "))
number2 = int(input("Second number: "))

print(f"{number1} + {number2} = {number1+number2}")



data = input("What is your name? ")
print("Hi " + data + "!")

data = int(input("What is your age? "))
# program continues...



# exercise 3

# Write your solution here
days=int(input("How many days?"))
seconds=days*24*60*60
print(f"Seconds in that many days {seconds}")


# exercise 4
# Fix the code
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)


# exercise 5
# Write your solution here
n1=int(input("Number 1:"))
n2=int(input("Number 2:"))
sum=n1 + n2
product=n1 * n2
print(f"The sum of the numbers: {sum}")
print(f"The product of the numbers: {product}")



# exercise 6
# Write your solution here
n1=int(input("Number 1 "))
n2=int(input("Number 2:"))
n3=int(input("Number 3:"))
n4=int(input("Number 4:"))
sum=n1 + n2 + n3 + n4
mean=sum/4

print(f"The sum of the numbers is {sum} and the mean is {mean}")

# exercise 7
# Write your solution here
days=int(input("How many times a week do you eat at the student cafeteria?"))
price=float(input("The price of a typical student lunch?"))
grocery=float(input("How much money do you spend on groceries in a week?"))
weekly=days*2.5+grocery
daily=weekly/7

print()
print("Average food expenditure:")
print(f"Daily: {daily:.1f} euros")
print(f"Weekly: {weekly} euros")



# Ask user inputs
meals_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
price_per_meal = float(input("The price of a typical student lunch? "))
groceries_per_week = float(input("How much money do you spend on groceries in a week? "))

# Calculations
cafeteria_total = meals_per_week * price_per_meal
weekly_total = cafeteria_total + groceries_per_week
daily_average = weekly_total / 7

# Output
print("\nAverage food expenditure:")
print(f"Daily: {daily_average} euros")
print(f"Weekly: {weekly_total} euros")