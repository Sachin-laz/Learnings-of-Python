print("Starting Python basics")
print("Updating the Code for git push")

x = "Sachin"
age = 24
if (x.find("sachin") != -1):
    print(x.center(20, "@"))
else:
    print("Someone else is trying")    
detail = {
    "Name":x,
    "Age":age
}

print(f"My name is ", detail["Name"], "\n I am ", detail["Age"], " Year old ")

#n = input(str("What is your name : "))
n = "sss"

print("My other name is {fname}".format(fname = n))

# String Basics

a = "String Basics"

print(a[2:5])

print(a.upper())

CodeName = 'Python'

print(f"I love {CodeName}")

print(10 > 9)
print(10 == 9)
print(bool("Hello"))
print(bool(-1))
print(u := 4)
print(u)