# Logical Operators - 
#       Evaluate multiple conditions (or,and,not) 
#       or = at least one condition must be true
#       and = both condtions must be True 
#       not=invertes the condition (not False, not True)

temp=40
is_raining=True
is_sunny=False
# or operator
if temp>35 or temp < 0 or is_raining:
    print("The outdoor event cancelled")
else:
    print("The outdoor event is still scheduled")

# and operator

if temp>=28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp<=0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")

# not Operator
if temp>=28 and not is_sunny:
    print("It is HOT outside")
    print("It is Cloudy")
elif temp<=0 and not is_sunny:
    print("It is COLD outside")
    print("It is Cloud")
elif temp < 28 and temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is Cloudy")




