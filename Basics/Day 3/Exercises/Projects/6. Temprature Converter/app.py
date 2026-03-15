temp=int(input("Enter Temprature in Farenheit or Celcius = "))
degree=input("Enter the degree F for Farenheit and C for Celcius = ")

# $$C = (F - 32) \div 1.8$$
if(degree=="C"):
    C=(temp - 32)/1.8
    print(f"{C:.2f} temprature in celcius")
# $$F = (C \times 1.8) + 32$$ 
elif(degree=="F"):
    F=(temp*1.8)+32
    print(f"{F:.2f} temprature in Farenheit")
else:
    print("You did not enter a valid temprature degree")