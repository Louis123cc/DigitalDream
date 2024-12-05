mytuple = ('joy', 'man', 'woman', 'age')
# for x in mytuple:
#     print(x)
# myiter = iter(mytuple)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# my = "Banana"
# myit = iter(my)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# class Mynumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
    
# myclass = Mynumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class mynumbers:
#     def __iter__(self):
#         self.x = 1
#         return self
#     def __next__(self):
#         if self.x <= 20:
#          y = self.x
#          self.x += 1
#          return  y
#         else:
#          raise StopIteration
        
# myclass = mynumbers()
# ite = iter(myclass)
# for x in ite:
#     print(x)

# class car:
#    def __init__(self, brand, model):
#       self.brand = brand
#       self.model = model
#       def move(self):
#          print("Driving!!")

# class Boat:
#    def __init__(self, brand, model) -> None:
#       self.brand = brand
#       self.model = model
#       def move(self):
#          print("Sailing!!")

# class Plane:
#    def __init__(self, brand, model) -> None:
#       self.brand = brand
#       self.model = model
#       def move(self):
#          print("we are flying !!")


# car1 = car("Ford", "Mustang")
# boat1 = Boat("sea eagle", "soaring")
# plane1 = Plane("Boeing", "456")
# for x in

   
listitems= ['chair', 'bed', 'cup', 'curtain', 'table']
item= iter(listitems)
for x in item:
    print(x)

num = 50
num2 = 100
def Show():
    xy = 46
    print(num + num2, xy)
    def moreShow():
        global yz 
        yz = 100
        print(xy, yz, num, num2)
        
    print(num, num2, xy)
    return moreShow()

Show()
print(yz)


import function
import index

function.multiply(30,20)
print(index.item1)


import datetime
time = datetime.datetime.now()
print(time.second)


"New class Begins python math"
x = min( 20, 9, 3)
y = max (20, 12, 30)
z = pow(5, 10)
import math
import json

square = math.sqrt(100)
ceilig = math.ceil(20.6)
flooring = math.floor(20.6)
print(ceilig)
print(flooring)
print(square)
print(math.pi * 21)

userdetails = '{"Name": "Louis", "Age": 23, "Height": 52}'
print(userdetails)

converted = json.dumps(userdetails)
loader = json.loads(userdetails)
print(loader["Name"])

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x, indent= 3, separators=(",", "=")))


"Regular expression"
import re

txt = "The rain in spain is the main pain"
discovered = re.search('ai', txt)
print(discovered.span())

lister = re.split(" ", txt)
print(lister)

threeDots = re.sub("a", "9", txt)
print(threeDots)

import camelcase
camel = camelcase.CamelCase()
print(camel.hump(txt))


"New class 'Try...Except"
try:
    result = 20/0
    print(result)
except:
    print("An error occured go back")

print("New class")
print("New class")



try:
    main = 20/0
    print(main)
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("An error occured")
except:
    print("Push ahead ")


# f = open("file.txt", 'a')
# f.write("Now the file has a new begining")
# f.write('this is a text file used only for python class')

# f.close()
# f = open("file.txt")
# print(f.read())

import os
os.remove("file.txt")
