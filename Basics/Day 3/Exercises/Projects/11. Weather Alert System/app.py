temp=int(input("Enter a temprature = "))
condition=input("Enter a weather condition cold,hot,cool = ")
if(temp > 30 and condition=="hot"):
    print(f"{temp} is temprature don't go outside it's {condition} outside")
elif(temp <0 and condition=="cold"):
    print(f"{temp} is temprature don't go outside it's {condition} outside")
elif(temp>0 and condition=='cool'):
    print(f"{temp} is temprature you can go outside it's {condition} outside")
else:
    print("Don't go outside we did not know the temprature and condition outside")