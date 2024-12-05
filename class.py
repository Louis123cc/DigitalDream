class Add:
    x = 10
    y = 20 
    z = 30
    def __init__(self, x, y, z) -> None:
        self.num1 = x
        self.num2 = y
        self.num3 = z

    def addition (self):
        finalresult = self.num1 + self.num2 + self.num3
        print(finalresult)
        return(finalresult)

# the self is constant while using the class 
# also self is the future object you are going to create 

nums = Add(10,20,30) 
myObj = Add(100,200,50)
obj2 = Add(30,10,50)



print(myObj.num1)
final = myObj.num2 + 50
sub = obj2.num3 * 20
obj2.addition()

# print(sub)
# print(final)

# final 


# print(nums.x)
# final = nums.y + 70
# print(nums.z + final)


class Add:
    x = 20
    y = 30
    z = 13
    def __init__(self, x, y, z) -> None:
        self.num = x
        self.num1 = y
        self.num2 = z

numbers = Add(23,12,10)
ages = Add(12, 15, 26)
pages = Add (11, 24, 10)  
result = ages.num *23
print(result)
print(ages.num2)

class Person:
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address
    def __str__(self) -> str:
        return f"{self.name}({self.age}){self.address}"
    def myfunc(self):
        print("hello my name is " + self.name + ' i am ' + str(self.age) + ' i live at ' + self .address)
    
person1 = Person("John", 23, '23 ezinifete street ' )
person1.myfunc()
print(person1)


class Parent:
    def __init__(self, fname, lname,Age) -> None:
        self. firstname = fname
        self.lastname = lname
        self.age = Age

    def printName(self):
        print(self.firstname, self.lastname, self.age)

x = Parent("Louis", "Christain", 30)
x.printName()


class Student(Parent):
    def __init__(self, fname, lname, age):
        self.name1 = fname
        self.name2 = lname
        self.lamba = age

    def printChild(self):
        print(self.name1, self.name2, self.lamba)
class()

y = ("Akachukwu", "raphael", 20)
x.printName()


