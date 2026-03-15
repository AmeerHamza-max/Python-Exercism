#   collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK.
#   Set = {} unordered and immutable, but Add/Remove OK.NO duplicates
#   Tuple = () ordered and unchangeable Duplicates OK. Faster

fruit="apple"


fruite=["apple","orange","banana","cocunut"]
# print(dir(fruite))
# print(help(fruite))
print(fruite)
print(len(fruite))
print("apple" in fruite)
# fruite[0]="pineapple"
# print("pineapple" in fruite)

# fruite.append("Gawa")
# fruite.remove("apple")
# fruite.insert(0,"pineapple")
# fruite.sort()
# fruite.reverse()
# fruite.clear()
print(fruite.index("orange"))

print(fruite[0])
print(fruite[1])
print(fruite[2])
print(fruite[3])
print(fruite[0:3])
print(fruite[::-1])

for fruite in fruite:
    print(fruite)




# Set
fruits={"apple","orange","banana","coconut","cocunut"}
print("apple" in fruits)
# print(fruits[0]) #Set are not iterable

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()




# Tuples

fruits=("apple","orange","banana","coconut","Gawa")
# print(dir(fruits))
# print(help(fruits))
print(fruits.index("apple"))
print(fruits.count("coconut"))


print(fruits)

for fruit in fruits:
    print(fruit)

