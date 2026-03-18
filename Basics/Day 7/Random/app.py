import random
# print(help(random))
# number=random.randint(1,6)
# print(number)



low=1
high=100
options=("rock","paper","scissors")
number=random.randint(low,high)
number=random.random()
cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
# print(number)

option=random.choice(options)
print(options)

random.shuffle(cards)
print(cards)