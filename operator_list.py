a = 15 
b = 4

print(a % b)
print(a // b)
print(a ** b)

# List Items

thisList = ["apple", "orrange", "mango"]
thisList.insert(2, "banana")
tropList = ["pineapple", "watermelon"]
tropList.append("mango")
thisList.extend(tropList)
print(thisList)
thisList.pop(0)
thisList.remove("orrange")
thisList.clear()
del tropList
print(thisList)

#loop in list 

animal = list(("lion", "tiger", "elephant", "panther"))
for i in animal:
    print(i)
for i in range(len(animal)):
    print(animal[i])

j = 0
while j < len(animal):
    print(f"This is {animal[j]}")
    j +=1


[print(x) for x in animal]